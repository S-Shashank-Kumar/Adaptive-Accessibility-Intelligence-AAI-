# Implementation Guide: Advanced Features

This guide explains how to implement, test, and deploy the advanced features of the AAI platform.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      FRONTEND (React/TypeScript)             │
├─────────────────────────────────────────────────────────────┤
│  AccessibilityPanel      MainContent      SignLanguageAvatar │
│  (Settings Management)   (Text I/O)       (ASL Animation)    │
└─────────────────────────────────────────────────────────────┘
                           │
                    HTTP/REST API
                           │
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                         │
├──────────────────────────────────────────────────────────────┤
│  Routes Layer                                                │
│  ├── /auth     (User registration/login)                    │
│  ├── /user     (Profile management)                         │
│  ├── /text     (Text simplification)                        │
│  ├── /avatar   (Sign language animation)                    │
│  └── /guided   (Step-by-step workflow)                      │
├──────────────────────────────────────────────────────────────┤
│  Services Layer                                              │
│  ├── AuthService      (JWT tokens, password hashing)        │
│  ├── TextAdapter      (NLP simplification)                  │
│  ├── SpeechService    (TTS/STT preprocessing)               │
│  ├── AvatarService    (ASL animation generation)            │
│  └── GuidedModeService(Workflow management)                 │
├──────────────────────────────────────────────────────────────┤
│  Models & Database                                           │
│  ├── User            (Email, password, timestamps)          │
│  ├── AccessibilityProfile (20+ settings)                    │
│  └── TextSimplification   (Caching, audit logs)             │
└─────────────────────────────────────────────────────────────┘
```

## Request/Response Flow

### Text Simplification Flow
```
1. User pastes text in MainContent
2. Click "Simplify This Text"
3. POST /api/v1/text/simplify
   ├── Backend validates text (10-5000 chars)
   ├── Checks for cached result
   ├── If not cached:
   │   ├── Loads Hugging Face BART model
   │   ├── Generates summarization with reading_level ratio
   │   ├── Falls back to rule-based if ML fails
   │   └── Caches result in database
   └── Returns: { simplified_text, reading_level, processing_time }
4. Frontend displays simplified text with applied CSS settings
5. Optional: Generate avatar animation with POST /api/v1/avatar/sign
6. Optional: Read aloud with Web Speech API
```

### Avatar Generation Flow
```
1. User has simplified text
2. Click "Show Avatar" button
3. POST /api/v1/avatar/sign
   ├── Backend validates text (max 1000 chars)
   ├── Splits text into words
   ├── Looks up each word in ASL_DICTIONARY:
   │   ├── If recognized: Returns video filename
   │   ├── If not recognized: Marks for fingerspelling
   │   └── Duration: ~1500ms per sign, ~200ms per letter
   └── Returns: {
        text, word_count, recognized_words, animations[], 
        total_duration_ms, avatar_speed
      }
4. Frontend renders SignLanguageAvatar component
5. Avatar generates animation sequence
6. User clicks Play to start animation
7. User can pause, reset, or click specific word to jump
```

### Guided Mode Flow
```
1. User enables Guided Mode in AccessibilityPanel
2. Frontend shows Step 1 (Welcome Page)
3. User clicks "Start" button
4. Frontend transitions to Step 2 (Paste Text)
   ├── GET /api/v1/guided/instructions/paste_text
   └── Receives: Title, description, button label, validation rules
5. User pastes text (minimum 10 characters)
6. User clicks "Next"
   ├── POST /api/v1/guided/next
   │   ├── Backend validates: len(text) >= 10
   │   └── Returns Step 3 instructions
7. User selects reading level
8. User clicks "Next"
   ├── POST /api/v1/guided/next
   │   ├── Backend validates: reading_level selected
   │   └── Returns Step 4 (Simplify - processing state)
9. Backend processes text (API call)
10. Auto-transitions to Step 5 (Review)
11. User reviews simplified text
12. User clicks "Done" or "Next"
    ├── POST /api/v1/guided/next
    └── Returns Step 6 (Complete - ask about next text)
13. User can start over or exit guided mode
```

## Service Implementation Details

### TextAdapter Service

#### ML-Based Simplification
```python
# Using Hugging Face BART model
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def simplify_text(text: str, reading_level: str):
    # Reading level to summary ratio mapping
    ratio_map = {
        "basic": 0.35,        # Keep 35% = remove 65%
        "intermediate": 0.50, # Keep 50%
        "advanced": 0.75      # Keep 75%
    }
    ratio = ratio_map.get(reading_level, 0.50)
    
    # Calculate max_length (words to keep)
    max_length = max(50, int(len(text.split()) * ratio))
    
    # Generate summary
    summary = summarizer(text, max_length=max_length, min_length=30)
    return summary[0]["summary_text"]
```

#### Fallback Rule-Based Simplification
```python
def simplify_text_rule_based(text: str, reading_level: str):
    sentences = text.split('. ')
    removal_rate = {"basic": 0.65, "intermediate": 0.50, "advanced": 0.25}
    rate = removal_rate.get(reading_level, 0.5)
    
    keep_count = max(1, int(len(sentences) * (1 - rate)))
    kept_sentences = sentences[:keep_count]
    
    # Remove parenthetical info
    result = '. '.join(kept_sentences)
    result = re.sub(r'\([^)]*\)', '', result)
    
    return result
```

### AvatarService Service

#### ASL Dictionary
```python
ASL_DICTIONARY = {
    "hello": "asl_hello.mp4",
    "thank": "asl_thank.mp4",
    "family": "asl_family.mp4",
    ...  # 20+ common words
}

def text_to_sign_animation(text: str) -> dict:
    words = text.lower().split()
    animations = []
    
    for word in words:
        if word in ASL_DICTIONARY:
            # Use recorded ASL sign
            animations.append({
                "word": word,
                "video": ASL_DICTIONARY[word],
                "duration": 1500,
                "recognized": True
            })
        else:
            # Spell out with fingerspelling
            animations.append({
                "word": word,
                "letters": list(word.upper()),
                "type": "fingerspell",
                "duration": len(word) * 200,
                "recognized": False
            })
    
    return {
        "text": text,
        "animations": animations,
        "total_duration_ms": sum(a["duration"] for a in animations)
    }
```

### GuidedModeService Service

#### Step Definitions
```python
class GuidedStep(Enum):
    WELCOME = "welcome"       # 1
    PASTE_TEXT = "paste_text" # 2
    SELECT_OPTIONS = "select_options" # 3
    SIMPLIFY = "simplify"     # 4
    REVIEW = "review"         # 5
    COMPLETE = "complete"     # 6

STEP_SEQUENCE = [
    GuidedStep.WELCOME,
    GuidedStep.PASTE_TEXT,
    GuidedStep.SELECT_OPTIONS,
    GuidedStep.SIMPLIFY,
    GuidedStep.REVIEW,
    GuidedStep.COMPLETE,
]
```

#### Step Navigation
```python
def get_next_step(current: GuidedStep) -> Optional[GuidedStep]:
    index = STEP_SEQUENCE.index(current)
    if index < len(STEP_SEQUENCE) - 1:
        return STEP_SEQUENCE[index + 1]
    return None

def get_previous_step(current: GuidedStep) -> Optional[GuidedStep]:
    index = STEP_SEQUENCE.index(current)
    if index > 0:
        return STEP_SEQUENCE[index - 1]
    return None

def validate_step(step: GuidedStep, data: dict) -> Tuple[bool, Optional[str]]:
    if step == GuidedStep.PASTE_TEXT:
        if len(data.get("text", "").strip()) < 10:
            return False, "Text too short"
    elif step == GuidedStep.SELECT_OPTIONS:
        if not data.get("reading_level"):
            return False, "Please select reading level"
    return True, None
```

### SpeechService Service

#### Text Preparation
```python
def prepare_text_for_speech(text: str, max_length: int = 500) -> str:
    # Replace special characters
    text = text.replace("&", "and")
    text = text.replace("@", "at")
    text = text.replace("#", "number")
    text = text.replace("_", " ")
    
    # Limit length
    if len(text) > max_length:
        sentences = text.split(". ")
        result = ""
        for sentence in sentences:
            if len(result) + len(sentence) < max_length:
                result += sentence + ". "
            else:
                break
        return result
    return text

def split_text_for_tts(text: str, max_utterance_length: int = 500):
    """Break text into safe chunks for TTS"""
    chunks = []
    sentences = text.split(". ")
    current = ""
    
    for sentence in sentences:
        if len(current) + len(sentence) < max_utterance_length:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    
    if current:
        chunks.append(current.strip())
    
    return chunks
```

## Database Schema

### User Model
```python
class User(Base):
    __tablename__ = "users"
    
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, unique=True)
    full_name: str = Column(String)
    hashed_password: str = Column(String)
    is_active: bool = Column(Boolean, default=True)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, onupdate=datetime.utcnow)
    
    accessibility_profile: "AccessibilityProfile" = relationship("AccessibilityProfile")
    simplifications: "TextSimplification" = relationship("TextSimplification")
```

### AccessibilityProfile Model
```python
class AccessibilityProfile(Base):
    __tablename__ = "accessibility_profiles"
    
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    
    # Visual Adjustments
    font_size: int = Column(Integer, default=16)  # 12-32
    line_spacing: float = Column(Float, default=1.5)  # 1.0-3.0
    letter_spacing: float = Column(Float, default=0)  # 0-2
    font_family: str = Column(String, default="system")
    color_overlay: str = Column(String, default="none")
    high_contrast: bool = Column(Boolean, default=False)
    dark_mode: bool = Column(Boolean, default=False)
    
    # Content Controls
    simplify_text: bool = Column(Boolean, default=True)
    reading_level: str = Column(String, default="intermediate")
    
    # Interaction
    speech_rate: float = Column(Float, default=1.0)
    reduce_motion: bool = Column(Boolean, default=False)
    reduce_animation: bool = Column(Boolean, default=False)
    sound_enabled: bool = Column(Boolean, default=True)
    vibration_enabled: bool = Column(Boolean, default=False)
    
    # Advanced
    minimal_mode: bool = Column(Boolean, default=False)
    guided_mode: bool = Column(Boolean, default=False)
    show_avatar: bool = Column(Boolean, default=False)
    
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, onupdate=datetime.utcnow)
```

### TextSimplification Model (Caching)
```python
class TextSimplification(Base):
    __tablename__ = "text_simplifications"
    
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    original_text: str = Column(String(5000))
    simplified_text: str = Column(String(2500))
    reading_level: str = Column(String)  # basic, intermediate, advanced
    processing_time_ms: int = Column(Integer)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
```

## Frontend Component Architecture

### MainContent Component
```typescript
interface MainContentProps {
  settings: AccessibilitySettings;
}

// State Management
- inputText: string
- simplifiedText: string
- loading: boolean
- error: string
- speechActive: boolean
- showAvatar: boolean

// Key Functions
- handleSimplify(): POST /api/v1/text/simplify
- handleReadAloud(): Web Speech API TTS
- handleDictate(): Web Speech API STT
- handleCopy(): clipboard.writeText()

// Conditional Renders
- Show error message (role="alert")
- Show SignLanguageAvatar (if showAvatar && simplifiedText)
- Show simplified text output
- Show read aloud/copy/dictate buttons
- Show avatar toggle button (if settings.showAvatar)
```

### SignLanguageAvatar Component
```typescript
interface SignLanguageAvatarProps {
  text: string;
  isVisible: boolean;
  onComplete?: () => void;
}

// State Management
- avatarData: AvatarData | null
- currentWordIndex: number
- isPlaying: boolean
- error: string

// Key Functions
- generateAvatarAnimation(): POST /api/v1/avatar/sign
- playAnimation(): Sequential animation through words
- pauseAnimation(): Stop animation
- resetAnimation(): Return to start

// Display Elements
- SVG avatar figure
- Current word display
- Play/Pause/Reset buttons
- Progress bar
- Word chips for navigation
- Statistics (recognized/total, duration)
```

## Testing Strategy

### Backend Unit Tests
```python
# test_avatar.py
def test_text_to_sign_animation():
    result = AvatarService.text_to_sign_animation("hello world")
    assert len(result["animations"]) == 2
    assert result["total_duration_ms"] > 0

def test_sign_language_endpoint():
    response = client.post("/api/v1/avatar/sign",
                          json={"text": "hello"},
                          headers={"Authorization": "Bearer token"})
    assert response.status_code == 200
```

```python
# test_guided.py
def test_validate_step_completion():
    is_valid, error = GuidedModeService.validate_step_completion(
        GuidedStep.PASTE_TEXT,
        {"text": "short"}
    )
    assert is_valid is False
    assert error is not None
```

### Frontend Component Tests
```typescript
// MainContent.test.tsx
test("should display simplified text", async () => {
  const { getByText } = render(<MainContent settings={mockSettings} />);
  const input = getByText(/paste complex text/i);
  fireEvent.change(input, { target: { value: "complex text..." } });
  fireEvent.click(getByText("Simplify"));
  
  await waitFor(() => {
    expect(getByText(/simplified text/i)).toBeInTheDocument();
  });
});

test("should show avatar when enabled", () => {
  const settings = { ...mockSettings, showAvatar: true };
  const { getByText } = render(<MainContent settings={settings} />);
  // Test avatar visibility
});
```

### Integration Tests
```python
# E2E test: Full workflow
async def test_complete_simplification_workflow():
    # 1. Register user
    register_response = client.post("/api/v1/auth/register", ...)
    user_id = register_response.json()["id"]
    token = register_response.json()["access_token"]
    
    # 2. Simplify text
    simplify_response = client.post("/api/v1/text/simplify",
                                    json={"text": "..."},
                                    headers={"Authorization": f"Bearer {token}"})
    simplified = simplify_response.json()["simplified_text"]
    
    # 3. Generate avatar
    avatar_response = client.post("/api/v1/avatar/sign",
                                  json={"text": simplified},
                                  headers={"Authorization": f"Bearer {token}"})
    
    assert avatar_response.status_code == 200
    assert "animations" in avatar_response.json()["avatar_data"]
    
    # 4. Update user profile with Avatar enabled
    profile_response = client.put("/api/v1/user/profile",
                                  json={"show_avatar": True},
                                  headers={"Authorization": f"Bearer {token}"})
    
    assert profile_response.json()["show_avatar"] is True
```

## Performance Optimization

### Caching Strategy
```python
# Database caching for text simplification
def simplify_text(text: str, reading_level: str):
    # Check database cache
    cached = db.query(TextSimplification).filter(
        TextSimplification.original_text == text,
        TextSimplification.reading_level == reading_level
    ).first()
    
    if cached:
        return cached.simplified_text
    
    # Compute if not cached
    result = expensive_ml_operation(text)
    
    # Save to cache
    db.add(TextSimplification(
        user_id=user_id,
        original_text=text,
        simplified_text=result,
        reading_level=reading_level
    ))
    db.commit()
    
    return result
```

### Frontend Performance
```typescript
// Lazy load avatar component
const SignLanguageAvatar = lazy(() => 
  import('./SignLanguageAvatar')
);

// Memoize settings to prevent unnecessary re-renders
const MemoizedAccessibilityPanel = memo(AccessibilityPanel);

// Debounce speech rate changes
const debouncedSpeechRateChange = debounce((rate) => {
  updateSetting("speechRate", rate);
}, 300);
```

## Deployment Checklist

- [ ] Run `pytest` with 80%+ coverage
- [ ] Run frontend tests with Jest
- [ ] Validate Pydantic schema validation
- [ ] Test all API endpoints with Postman/REST Client
- [ ] Test keyboard navigation thoroughly
- [ ] Test screen reader compatibility
- [ ] Performance test with 100+ concurrent users
- [ ] Security audit (CORS, headers, authentication)
- [ ] Database migration scripts created
- [ ] Environment variables documented
- [ ] CI/CD pipeline configured in GitHub Actions
- [ ] Staging environment tested
- [ ] Production deployment verified
- [ ] Monitoring and logging enabled

## Monitoring & Logging

### Backend Logging
```python
import logging

logger = logging.getLogger(__name__)

logger.info(f"User {user_id} simplified text in {processing_time}ms")
logger.error(f"ML model failed: {error}, using fallback")
logger.debug(f"Avatar generated {word_count} words")
```

### Frontend Error Tracking
```typescript
// Send errors to monitoring service
window.addEventListener('error', (event) => {
  reportError({
    type: 'javascript',
    message: event.message,
    stack: event.error.stack,
    timestamp: new Date().toISOString()
  });
});
```

## Troubleshooting

### Avatar Not Showing
1. Check if `settings.showAvatar` is true
2. Verify text is not empty
3. Check backend `/api/v1/avatar/sign` response
4. Verify browser supports animations

### Guided Mode Not Advancing
1. Validate step completion: Check validation function
2. Check browser console for JS errors
3. Verify JWT token is valid
4. Test POST `/api/v1/guided/next` directly

### Speech Recognition Not Working
1. Check browser support (Chrome, Firefox, Safari, Edge)
2. Verify microphone permissions granted
3. Try different language or accent
4. Clear browser cache and retry

---

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [React Documentation](https://react.dev/)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [ARIA Standards](https://www.w3.org/WAI/ARIA/)

---

**Version**: 0.2.0
**Last Updated**: December 2024
