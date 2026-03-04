# Frontend Design & Accessibility Alignment Plan – AAI

**Document Purpose:** Align frontend UI/UX design with specific accessibility needs of diverse user groups. Ensures every feature, control, and interaction serves a real accessibility challenge.

**Last Updated:** March 3, 2026  
**Status:** Design Plan Ready for Implementation

---

## 1. Executive Summary

The AAI frontend must be **accessibility-first by design**, not accessibility-as-an-afterthought. Each UI component, control, and interaction must directly address one or more of the 6 core accessibility challenges:

1. **Dyslexia & Reading Comprehension** → Specialized fonts, color overlays, spacing controls
2. **ADHD & Cognitive Overload** → Reduced clutter, clear hierarchy, progressive disclosure
3. **Visual Impairments** → High contrast, large fonts, screen reader support, keyboard-only navigation
4. **Auditory Impairments** → Visual captions, sound indicators, sign language
5. **Motor/Speech Difficulties** → Minimal clicking, keyboard-friendly, voice input, predictive typing
6. **Neurodiverse Interaction Needs** → Customization, animation control, simple language, minimal distraction

---

## 2. User Persona Mapping & Core Needs

### 2.1 Dyslexia & Reading Comprehension

**User Profile:**
- Struggle with traditional fonts (especially serifs)
- Get confused by similar-looking letters (b/d, p/q)
- Need visual breaks and spacing
- Benefit from color overlays to reduce visual stress
- Read slower, need simplified language

**Frontend Requirements:**
| Need | Feature | UI Component | Behavior |
|------|---------|--------------|----------|
| Dyslexia-friendly font | Font selector in panel | Dropdown: "OpenDyslexic", "Arial", "Verdana" | Apply `font-family` to body, persist in localStorage |
| Line spacing | Spacing slider | Slider: 1.0x → 3.0x | Apply `line-height` CSS |
| Letter spacing | Letter spacing control | Slider: 0px → 2px | Apply `letter-spacing` CSS |
| Color overlays | Overlay color picker | Color palette: blue, green, yellow, sepia | Apply semi-transparent overlay to text background |
| Text simplification | Auto-simplify toggle | Toggle: "Simplify Language" | Call `/api/text/simplify` with `reading_level: "basic"` |
| Text alignment | Justify toggle | Toggle: "Left-aligned text" | Disable text-justify, use left alignment |

---

### 2.2 ADHD & Cognitive Overload

**User Profile:**
- Overwhelmed by too much visual information
- Needs clear, obvious hierarchy
- Benefits from focus zones (one task at a time)
- Distracted by movement/animations
- Needs clear progress indicators

**Frontend Requirements:**
| Need | Feature | UI Component | Behavior |
|------|---------|--------------|----------|
| Reduce visual clutter | Minimal mode | Toggle: "Minimal Layout" | Hide non-essential UI, show only active control panel |
| Clear hierarchy | Focus panel | Highlight current task area | CSS: border-glow, background contrast |
| Disable animations | Motion control | Toggle: "Reduce Motion" | Apply `prefers-reduced-motion: reduce` |
| Task focus | Step-by-step wizard | Button: "Guided Mode" | Show tasks sequentially: 1) Paste text 2) Simplify 3) Read aloud 4) Respond |
| Progress indication | Status badges | Show: "✓ Text pasted", "→ Simplifying...", "✓ Done" | Dynamic UI state |
| Hide auto-play content | Media control | Always require play action | No autoplay video/audio |

---

### 2.3 Visual Impairments

**User Profile:**
- Cannot see small text or low contrast
- Rely on screen readers (NVDA, JAWS)
- Use keyboard navigation exclusively
- Need semantic HTML and ARIA labels
- Benefit from high contrast and enlarged fonts

**Frontend Requirements:**
| Need | Feature | UI Component | Behavior |
|------|---------|--------------|----------|
| Large fonts | Font size control | Slider: 12px → 32px | Apply `font-size` to all text |
| High contrast | Contrast boost | Toggle: "High Contrast Mode" | Switch to black-on-white color scheme |
| Dark/Light modes | Theme switcher | Toggle: "Dark Mode" | Apply dark/light CSS theme |
| Keyboard navigation | Tab order | All interactive elements focusable | `tabindex` on buttons, proper focus styles |
| Screen reader support | ARIA labels | Every button/input has `aria-label` | `<button aria-label="Read aloud">🔊</button>` |
| Skip links | Jump navigation | Skip to main content | `<a href="#main-content">Skip to content</a>` |
| Semantic HTML | Proper markup | Use `<button>`, `<label>`, `<fieldset>` | Never `<div onclick>`, always semantic elements |
| Focus indicators | Visible focus ring | Show on all interactive elements | CSS: `outline: 3px solid blue` on focus |
| Alternative text | Image descriptions | Alt text for all visuals | `<img alt="Complex chart: Y-axis shows...">` |

---

### 2.4 Auditory Impairments

**User Profile:**
- Cannot hear audio or speech
- Need visual equivalents for all sound
- Benefit from sign language options
- Cannot use audio-based authentication

**Frontend Requirements:**
| Need | Feature | UI Component | Behavior |
|------|---------|--------------|----------|
| Text-to-speech visual feedback | Transcription display | Show text being spoken | Display current word highlighted in real-time |
| Captions for audio | Captions/transcript panel | Display TTS transcript | `<div aria-live="polite">Speaking: "...text here..."</div>` |
| Sign language avatar | Avatar video | Show ASL/sign translation | Embed video/animation of sign language |
| Visual sound indicators | Status icons | Show when audio is playing | Icon: 📢 (speaking), ⏸ (paused), ⏹ (stopped) |
| No audio-only content | Alternative formats | Always provide text/visual alternative | Never rely on audio alone for critical info |
| Vibration feedback (optional) | Haptic response | Optional: vibrate on completion | For mobile devices |

---

### 2.5 Motor/Speech Difficulties

**User Profile:**
- Cannot use mouse effectively (tremors, limited mobility, paralysis)
- Cannot speak clearly or at all
- Benefit from predictive typing
- Need reduced clicking/interactions
- Alternative input methods needed

**Frontend Requirements:**
| Need | Feature | UI Component | Behavior |
|------|---------|--------------|----------|
| Keyboard-only interface | No mouse required | All functions via Tab + Enter | Test without mouse |
| Larger click targets | Button sizing | Min 48x48px buttons | `min-height: 48px; min-width: 48px` |
| Skip repeated actions | Auto-fill/memory | Save last used settings | localStorage persistence |
| Predictive text | Auto-suggestion | Show word suggestions while typing | Call `/api/text/predict` for suggestions |
| Speech-to-text | Voice input button | Activate with key or button | Use Web Speech API (browser-native) |
| Text-to-speech | Read aloud button | Large, obvious button | Click → browser TTS |
| Reduce interactions | Combine actions | Pre-fill common tasks | Buttons do multiple things in sequence |
| Adjustable text speed | Speed control (if TTS) | Slider: 0.5x → 2x playback | Apply `speechRate` parameter |

---

### 2.6 Neurodiverse Interaction Needs

**User Profile:**
- Autism spectrum: needs predictability, clear patterns, minimal sensory input
- ADHD: needs immediate feedback, clear cause-effect
- Sensory processing issues: needs to control stimulation (animations, sounds)
- Communication challenges: benefits from structured inputs

**Frontend Requirements:**
| Need | Feature | UI Component | Behavior |
|------|---------|--------------|----------|
| Predictable layout | Consistent placement | Controls always in same location | Fixed sidebar, no moving elements |
| Clear cause-effect | Immediate feedback | Show action results instantly | "Simplify" button → instant text change |
| Animation control | Disable animations | Toggle: "Reduce Motion" | Remove fade-ins, slide transitions |
| Minimal notifications | Limited alerts | Only critical messages | Avoid toast notifications spam |
| Structured inputs | Form templates | Pre-defined forms, not free text | Dropdowns, checkboxes, not open textarea |
| Clear error messages | Specific feedback | "Email required" not just "Error" | `aria-live="assertive"` error announcements |
| Consistent terminology | Simple language | Use same words consistently | "Simplify" always, never "Digest" or "Reduce" |
| Sensory control | Vibration/sound toggle | Disable all vibration/beeps | `<input type="checkbox" aria-label="Enable sounds">` |

---

## 3. Frontend Component Architecture (Accessibility-Aligned)

### 3.1 Master Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                         HEADER                                   │
│   [AAI Logo]  [Font Size] [Contrast] [Help]  [Profile]          │
└─────────────────────────────────────────────────────────────────┘
┌──────────────────┬────────────────────────────────────────────────┐
│                  │                                                 │
│ ACCESSIBILITY    │            MAIN CONTENT AREA                    │
│ CONTROL PANEL    │                                                 │
│                  │  ┌──────────────────────────────────────────┐  │
│ ☑ Dark Mode      │  │                                           │  │
│ ☑ High Contrast  │  │     [Paste/Input Area or Article]        │  │
│ ☑ Dyslexia Font  │  │                                           │  │
│ ☑ Simplify Text  │  │     [Simplified Text Output]              │  │
│ ☑ Read Aloud     │  │     (with real-time highlighting)        │  │
│ ☑ Dictate        │  │                                           │  │
│ ☑ Show Avatar    │  │     [Sign Language Avatar]                │  │
│                  │  │                                           │  │
│ ≡ More Options   │  └──────────────────────────────────────────┘  │
│                  │                                                 │
│ [Reset All]      │  Status: ✓ Ready                              │
└──────────────────┴────────────────────────────────────────────────┘
```

### 3.2 Accessibility Control Panel (Sidebar)

**Location:** Fixed left sidebar (sticky, always visible)  
**Purpose:** All accessibility controls in one discoverable place  
**Accessibility:** Keyboard-navigable, proper ARIA labels

```tsx
// Structure
<aside aria-label="Accessibility Controls" role="complementary">
  <section aria-labelledby="visual-controls-heading">
    <h2 id="visual-controls-heading">Visual Adjustments</h2>
    <ControlGroup>
      <FontSizeSlider />
      <LineSpacingSlider />
      <LetterSpacingSlider />
      <FontSelector />
      <ColorOverlayPicker />
      <ContrastModeToggle />
    </ControlGroup>
  </section>

  <section aria-labelledby="content-controls-heading">
    <h2 id="content-controls-heading">Content</h2>
    <ControlGroup>
      <SimplifyToggle />
      <ReadingLevelSelector />
    </ControlGroup>
  </section>

  <section aria-labelledby="interaction-controls-heading">
    <h2 id="interaction-controls-heading">Interaction</h2>
    <ControlGroup>
      <ReadAloudButton />
      <DictateButton />
      <SpeechRateSlider />
    </ControlGroup>
  </section>

  <section aria-labelledby="motion-controls-heading">
    <h2 id="motion-controls-heading">Motion & Sensory</h2>
    <ControlGroup>
      <ReduceMotionToggle />
      <ReduceAnimationToggle />
      <SoundToggle />
      <VibrationToggle />
    </ControlGroup>
  </section>

  <section aria-labelledby="advanced-controls-heading">
    <h2 id="advanced-controls-heading">Advanced</h2>
    <DetailsDisclosure>
      <MinimalModeToggle />
      <GuidedModeToggle />
      <AvatarModeToggle />
      <ResetAllButton />
    </DetailsDisclosure>
  </section>
</aside>
```

### 3.3 Main Content Area

**Purpose:** Display and interact with actual content (articles, forms, etc.)

```tsx
<main id="main-content" role="main">
  <section aria-labelledby="input-heading">
    <h1 id="input-heading">Text Input</h1>
    <textarea 
      aria-label="Paste complex text here"
      aria-describedby="input-help"
      placeholder="Paste complex text or article..."
      style={{ minHeight: '150px' }}
    />
    <p id="input-help" className="help-text">
      Paste any complex text. We'll simplify it for you.
    </p>
    <button onClick={simplify}>Simplify This Text</button>
  </section>

  <section aria-labelledby="output-heading" className="results">
    <h2 id="output-heading">Simplified Text</h2>
    <div 
      className="text-output"
      aria-live="polite"
      aria-label="Simplified text output"
      style={{
        fontSize: `${fontSize}px`,
        lineHeight: `${lineSpacing}em`,
        letterSpacing: `${letterSpacing}px`,
        fontFamily: dislexiaFont ? 'OpenDyslexic' : 'inherit',
        ...colorOverlay,
        ...contrastMode,
      }}
    >
      {simplifiedText}
    </div>

    <div className="controls" role="group" aria-label="Output actions">
      <button onClick={readAloud} aria-label="Read aloud (press R)">
        🔊 Read Aloud
      </button>
      <button onClick={copToClipboard} aria-label="Copy to clipboard">
        📋 Copy
      </button>
      <button onClick={downloadAsFile} aria-label="Download as PDF">
        ⬇ Download
      </button>
    </div>
  </section>

  {showAvatar && (
    <section aria-labelledby="avatar-heading">
      <h2 id="avatar-heading">Sign Language Translation</h2>
      <SignLanguageAvatar 
        text={simplifiedText} 
        aria-label="Sign language animation"
      />
    </section>
  )}

  <section aria-labelledby="status-heading" className="status-bar">
    <h2 id="status-heading" className="sr-only">Status</h2>
    <div aria-live="polite" aria-atomic="true">
      {status} {loading && '⏳ Processing...'}
    </div>
  </section>
</main>
```

---

## 4. Accessibility Control Specifications

### 4.1 Visual Adjustments

#### Font Size Control
```
Slider: 12px → 32px
Default: 16px
Increments: 1px
Display: "Font Size: 16px"
Applies to: body, p, span, div
Persistence: localStorage
```

#### Line Spacing (for Dyslexia)
```
Slider: 1.0x → 3.0x
Default: 1.5x
Increments: 0.1x
Display: "Line Spacing: 1.5x"
CSS: line-height property
Persistence: localStorage
```

#### Letter Spacing (for Dyslexia)
```
Slider: 0px → 2px
Default: 0px
Increments: 0.1px
Display: "Letter Spacing: 0px"
CSS: letter-spacing property
Persistence: localStorage
```

#### Font Selector (Dyslexia-Friendly)
```
Options:
- System Default (inherit)
- OpenDyslexic (dyslexia-optimized)
- Arial (clean, sans-serif)
- Georgia (readable serif)
- Verdana (large x-height)
- Trebuchet MS (rounded)

Default: System Default
CSS: font-family
Persistence: localStorage
```

#### Color Overlay (for Visual Stress Reduction)
```
Palette:
- None (transparent)
- Light Blue (reduces glare)
- Green (calming)
- Yellow (warmth)
- Sepia (warm, aged paper feel)

Default: None
CSS: background-color with opacity 0.1-0.2
Applies to: text background only
Persistence: localStorage
```

#### High Contrast Mode
```
When enabled:
- Black text on white background
- 100% opacity (no transparency)
- Larger focus indicators (3px outline)
- Bold text for emphasis
- No subtle shadows/gradients

CSS: Switch to high-contrast color scheme
Persistence: localStorage
```

#### Dark Mode / Light Mode
```
Light Mode (default):
- Dark text on light background
- Gentle shadows

Dark Mode:
- Light text on dark background
- Reduced eye strain in low light
- Optional: Use system preference (prefers-color-scheme)

Persistence: localStorage
```

### 4.2 Content Controls

#### Simplify Text Toggle
```
Default: OFF
When enabled: Call `/api/text/simplify` on every input
Behavior: Replace source text with simplified version in real-time
Reading levels: "basic" (easiest) → "intermediate" → "advanced" (original)
```

#### Reading Level Selector
```
Options:
- Basic (grade 4-5 vocabulary)
- Intermediate (grade 7-8 vocabulary)
- Advanced (original complexity)

Default: Intermediate
Used by: Text simplification API
```

### 4.3 Interaction Controls

#### Read Aloud Button
```
Function: Use Web Speech API (browser native)
Keyboard shortcut: R key
When clicked:
- Start TTS on simplified text
- Highlight current word being spoken
- Show: [⏸ Pause] [⏹ Stop] [📈 Speed]
- Live region: "Reading aloud..."

Behavior:
- Highlights word by word in real-time
- Works offline (browser TTS, no API call)
- Adjustable speech rate: 0.5x → 2.0x
```

#### Dictate Button (Speech-to-Text)
```
Function: Use Web Speech API (browser native)
Keyboard shortcut: D key
When clicked:
- Open microphone
- Listen for speech
- Convert to text
- Populate input field
- Show: [🔴 Recording...] [Stop]

Behavior:
- Language: Auto-detect or user-selected
- Works offline (browser STT when available)
- Append to existing text or replace
```

#### Speech Rate Control
```
Slider: 0.5x → 2.0x playback speed
Default: 1.0x
Increments: 0.1x
Display: "Speech Rate: 1.0x"
Applies to: Read Aloud playback
Persistence: localStorage
```

### 4.4 Motion & Sensory Controls

#### Reduce Motion Toggle
```
When enabled:
- Disable all CSS animations
- Disable fade-ins, slide transitions
- Disable transitions on hover
- Apply: `prefers-reduced-motion: reduce` globally
- CSS: 0s transition-duration instead of animations

Applies to: All visual effects
Persistence: localStorage
```

#### Reduce Animation Toggle
```
Similar to Reduce Motion but more aggressive:
- Even smoother, more instant responses
- No spinning loaders (replace with static indicator)
- No slide-in panels (instant appear)
```

#### Sound Toggle
```
When disabled:
- Mute all audio effects
- Disable notification sounds
- Keep TTS muted until explicitly clicked

Applies to: Beeps, notifications, auto-play
Persistence: localStorage
```

#### Vibration Toggle
```
When disabled:
- Disable all haptic feedback (mobile)
- Disable vibration on button press
- Keep visual feedback (important!)

Applies to: navigator.vibrate() calls
Persistence: localStorage
```

### 4.5 Advanced Controls (Collapsible)

#### Minimal Mode
```
When enabled:
- Hide secondary nav, ads, decorative images
- Show only: Sidebar + Main content area
- Remove: Header images, footer, sidebars
- Hide: Explanatory text (keep labels)

Use case: Severe ADHD/cognitive overload
Persistence: localStorage
```

#### Guided Mode (Wizard)
```
When enabled:
- Show step-by-step instructions
- Lock UI to one section at a time
- Progress indicator: "Step 1 of 4"
- Auto-advance or manual next button

Sequence:
1. Paste/Input text (locked to textarea)
2. Click Simplify (only this button active)
3. Review simplified text (locked to output area)
4. Choose action: Read Aloud / Copy / Download

Use case: Overwhelming interface, ADHD, motor difficulties
```

#### Avatar Mode Toggle
```
When enabled:
- Show sign language avatar below simplified text
- Auto-generate sign animation with simplified text
- Toggle between: 2D avatar / 3D avatar / Video clip

Use case: Deaf/hard of hearing users
Persistence: localStorage
```

#### Reset All Button
```
When clicked:
- Clear localStorage of all accessibility settings
- Reset to system defaults
- Clear all input/output
- Confirm before resetting
```

---

## 5. Accessibility Feature Implementation (Phase-by-Phase)

### Phase 1: Frontend & SDK Foundation

#### Sprint 1.1: Core Layout & Basic Controls (Days 1-2)
- [x] Responsive sidebar layout (left sticky)
- [x] Keyboard navigation (Tab, Enter, Escape)
- [x] ARIA labels on all interactive elements
- [x] Semantic HTML (button, label, fieldset, aside, main)
- [x] Basic CSS variables for colors, fonts, spacing
- [x] localStorage integration for persistence

**Components to build:**
1. `AccessibilityPanel.tsx` — Main sidebar container
2. `FontSizeControl.tsx` — Font size slider + display
3. `ContrastModeToggle.tsx` — High contrast switcher
4. `ThemeToggle.tsx` — Dark/light mode toggle
5. `MainContentArea.tsx` — Content display with proper ARIA structure

**Deliverable:** Keyboard-navigable UI, all controls persist to localStorage

---

#### Sprint 1.2: Dyslexia-Friendly Features (Day 2)
- [x] OpenDyslexic font loading (Google Fonts)
- [x] Line spacing slider (1.0x → 3.0x)
- [x] Letter spacing slider (0px → 2px)
- [x] Font selector dropdown
- [x] Color overlay picker

**Components to build:**
1. `LineSpacingControl.tsx` — Slider + CSS application
2. `LetterSpacingControl.tsx` — Slider + CSS application
3. `FontSelector.tsx` — Dropdown with OpenDyslexic, Arial, Verdana, Georgia
4. `ColorOverlayPicker.tsx` — Color palette selector

**Deliverable:** Full dyslexia support operational (fonts, spacing, overlays)

---

#### Sprint 1.3: Motion & Sensor Controls (Day 3)
- [x] Reduce Motion toggle (CSS + animations)
- [x] Sound toggle (mute flag in state)
- [x] Simple theme switcher (no animations)

**Deliverable:** ADHD users can disable all motion

---

### Phase 2: API Integration & Core Features

#### Sprint 2.1: Read Aloud & Dictate (Days 2-3)
- [x] Read Aloud button → Web Speech API (SpeechSynthesisUtterance)
- [x] Word-by-word highlighting during playback
- [x] Speech rate control (0.5x → 2.0x)
- [x] Dictate button → Web Speech API (SpeechRecognition)
- [x] Real-time transcription display

**Components to build:**
1. `ReadAloudButton.tsx` — Trigger TTS, show playback controls
2. `WordHighlighter.tsx` — Highlight current word during speech
3. `SpeechRateControl.tsx` — Speed slider for TTS
4. `DictateButton.tsx` — Trigger STT, append to textarea
5. `TranscriptionDisplay.tsx` — Live transcription feedback

**Deliverable:** Full speech I/O via browser native APIs

---

#### Sprint 2.2: API Integration (Days 2-3)
- [x] Connect to `/api/text/simplify` endpoint
- [x] Connect to `/api/user/profile` endpoint
- [x] Load user settings on app mount
- [x] Save settings on change
- [x] Error handling & retry logic

**Deliverable:** Frontend fully integrated with backend

---

### Phase 3: AI Services & Avatar

#### Sprint 3.1: Sign Language Avatar (Days 4-5)
- [x] Sign language avatar component
- [x] Call to `/api/avatar/sign` endpoint
- [x] Display animated avatar (using library or video clips)
- [x] Toggle avatar on/off (Avatar Mode toggle in advanced settings)

**Components to build:**
1. `SignLanguageAvatar.tsx` — Display sign animation
2. `AvatarVideo.tsx` — Embed video or animation player
3. `AvatarModeToggle.tsx` — Enable/disable avatar

**Deliverable:** Sign language translation available for all simplified text

---

#### Sprint 3.2: Guided Mode (Wizard) Implementation (Day 5)
- [x] Step-by-step wizard UI
- [x] Progress indicator ("Step 1 of 4")
- [x] Lock UI to active section
- [x] Next/Previous navigation
- [x] Auto-advance on action completion

**Components to build:**
1. `GuidedModeWizard.tsx` — Main wizard container
2. `Step1Paste.tsx` — Input text step
3. `Step2Simplify.tsx` — Simplify action step
4. `Step3Review.tsx` — Review output step
5. `Step4Action.tsx` — Choose action (read/copy/download)
6. `ProgressIndicator.tsx` — Step counter

**Deliverable:** ADHD/overwhelmed users can use guided flow

---

### Phase 4: Performance & Caching

#### Sprint 4.1: Frontend Optimization (Day 6)
- [x] Debounce text input (avoid rapid API calls)
- [x] Memoize components (React.memo)
- [x] Lazy load avatar component
- [x] CSS optimization (no inline styles)

**Deliverable:** Responsive UI, < 3 second response times

---

### Phase 5: Security & Testing

#### Sprint 5.1: Testing for Accessibility (Day 7+)
- [x] Unit tests for each control (does toggle work? does slider apply CSS?)
- [x] Keyboard navigation tests (Tab through all controls)
- [x] Screen reader tests (NVDA/JAWS compatibility)
- [x] Color contrast tests (WCAG AA minimum)
- [x] Mobile accessibility tests (touch targets ≥ 48x48px)
- [x] Test each user persona flow (mock flow per accessibility need)

**Test Suites:**
1. `AccessibilityControls.test.tsx` — Slider/toggle functionality
2. `KeyboardNavigation.test.tsx` — Tab order, focus management
3. `ScreenReaderCompat.test.tsx` — ARIA label validation
4. `ContrastCompliance.test.tsx` — Color contrast ratios (automated)
5. `UserPersonaFlows.test.tsx` — Full flows for each user type
6. `SpeechIntegration.test.tsx` — Read aloud / dictate functionality

**Deliverable:** 80%+ test coverage, WCAG AA compliance

---

## 6. File Structure (Frontend Implementation)

```
frontend/
├── src/
│   ├── components/
│   │   ├── AccessibilityPanel/
│   │   │   ├── AccessibilityPanel.tsx          # Main sidebar
│   │   │   ├── index.ts
│   │   │   └── AccessibilityPanel.module.css
│   │   ├── ControlSections/
│   │   │   ├── VisualAdjustments.tsx           # Font, spacing, overlay
│   │   │   ├── ContentControls.tsx             # Simplify, reading level
│   │   │   ├── InteractionControls.tsx         # Read aloud, dictate
│   │   │   ├── MotionSensoryControls.tsx       # Motion, sound, vibration
│   │   │   └── AdvancedControls.tsx            # Minimal, guided, avatar
│   │   ├── Controls/
│   │   │   ├── FontSizeControl.tsx
│   │   │   ├── LineSpacingControl.tsx
│   │   │   ├── LetterSpacingControl.tsx
│   │   │   ├── FontSelector.tsx
│   │   │   ├── ColorOverlayPicker.tsx
│   │   │   ├── ContrastModeToggle.tsx
│   │   │   ├── ThemeToggle.tsx
│   │   │   ├── ReduceMotionToggle.tsx
│   │   │   ├── SoundToggle.tsx
│   │   │   ├── VibrationToggle.tsx
│   │   │   └── ResetAllButton.tsx
│   │   ├── Buttons/
│   │   │   ├── ReadAloudButton.tsx
│   │   │   ├── DictateButton.tsx
│   │   │   ├── SimplifyButton.tsx
│   │   │   └── ActionButton.tsx
│   │   ├── MainContent/
│   │   │   ├── MainContentArea.tsx
│   │   │   ├── TextInputArea.tsx
│   │   │   ├── SimplifiedTextOutput.tsx
│   │   │   └── StatusBar.tsx
│   │   ├── SignLanguageAvatar/
│   │   │   ├── SignLanguageAvatar.tsx
│   │   │   ├── AvatarVideo.tsx
│   │   │   └── AvatarAnimation.tsx
│   │   ├── GuidedMode/
│   │   │   ├── GuidedModeWizard.tsx
│   │   │   ├── Step1Paste.tsx
│   │   │   ├── Step2Simplify.tsx
│   │   │   ├── Step3Review.tsx
│   │   │   ├── Step4Action.tsx
│   │   │   └── ProgressIndicator.tsx
│   │   ├── Common/
│   │   │   ├── KeyboardHint.tsx               # Show keyboard shortcut hints
│   │   │   ├── HelpIcon.tsx                   # ? icon with tooltip
│   │   │   ├── AccessibilityAnnouncement.tsx  # aria-live region
│   │   │   └── FocusManager.tsx               # Manage focus traps
│   │   └── Header/
│   │       ├── Header.tsx
│   │       └── Nav.tsx
│   ├── hooks/
│   │   ├── useAccessibilitySettings.ts        # Get/set from localStorage
│   │   ├── useTextSimplification.ts           # Call API
│   │   ├── useSpeechI.ts                       # TTS/STT logic
│   │   ├── useKeyboardNavigation.ts           # Global shortcuts (R, D, etc.)
│   │   └── useColorContrast.ts                # Manage contrast dynamically
│   ├── services/
│   │   ├── api.ts                             # Backend API calls
│   │   ├── speech.ts                          # Web Speech API wrapper
│   │   ├── storage.ts                         # localStorage wrapper
│   │   └── analytics.ts                       # Track feature usage
│   ├── styles/
│   │   ├── index.css                          # Global styles
│   │   ├── variables.css                      # CSS custom properties
│   │   ├── accessibility.css                  # ARIA styles, focus rings
│   │   ├── themes/
│   │   │   ├── light.css
│   │   │   ├── dark.css
│   │   │   └── high-contrast.css
│   │   ├── dyslexia-friendly.css              # Font, spacing tweaks
│   │   └── responsive.css                     # Mobile-first breakpoints
│   ├── types/
│   │   ├── accessibility.ts                   # Type defs
│   │   └── api.ts
│   ├── App.tsx                                # Main app component
│   ├── index.tsx                              # Entry point
│   └── __tests__/
│       ├── AccessibilityPanel.test.tsx
│       ├── KeyboardNavigation.test.tsx
│       ├── ScreenReaderCompat.test.tsx
│       ├── UserPersonaFlows.test.tsx
│       ├── SpeechIntegration.test.tsx
│       └── fixtures/
│           └── mockAccessibilitySettings.ts
├── public/
│   ├── index.html
│   └── assets/
│       └── asl-avatars/
│           └── prebuilt-clips/              # ASL video clips
├── package.json
├── tsconfig.json
├── jest.config.js
└── .env.example
```

---

## 7. Component-to-Accessibility Mapping

| Component | Accessibility Need | User Group(s) |
|-----------|-------------------|---|
| FontSizeControl | Text visibility | Visual impairments |
| LineSpacingControl | Reduce visual crowding | Dyslexia, visual stress |
| LetterSpacingControl | Letter differentiation | Dyslexia (b/d confusion) |
| FontSelector | Reading support | Dyslexia (OpenDyslexic) |
| ColorOverlayPicker | Visual stress reduction | Dyslexia, sensory sensitivity |
| ContrastModeToggle | Text readability | Visual impairments, neurodiverse |
| ThemeToggle | Eye comfort | Visual impairments, sensory sensitivity |
| ReadAloudButton | Audio access | Visual impairments, motor, dyslexia |
| DictateButton | Voice input | Motor/speech difficulties |
| SpeechRateControl | Pace customization | ADHD, processing speed variation |
| ReduceMotionToggle | Sensory overload reduction | ADHD, neurodiverse, epilepsy |
| SoundToggle | Auditory control | ADHD, sensory sensitivity, autism |
| VibrationToggle | Tactile control | Sensory sensitivity |
| SignLanguageAvatar | Deaf/HoH access | Auditory impairments |
| GuidedModeWizard | Cognitive support | ADHD, cognitive overload |
| MinimalModeToggle | Visual clutter reduction | ADHD, cognitive overload, autism |
| WordHighlighter | Visual tracking | ADHD, dyslexia, visual processing |

---

## 8. Keyboard Shortcuts (Accessibility-First)

All shortcuts optional, visible, and remappable:

```
Global Shortcuts:
R              →  Read Aloud (start/stop/pause)
D              →  Dictate (start/stop listening)
S              →  Simplify (process text)
C              →  Copy to clipboard
Ctrl+Z         →  Undo last simplification
Esc            →  Close any open dialog
Tab            →  Navigate between controls
Shift+Tab      →  Navigate backwards
Enter          →  Activate focused button
Space          →  Toggle checkbox/button

Accessibility Panel Navigation:
Alt+1          →  Jump to Visual Adjustments section
Alt+2          →  Jump to Content Controls section
Alt+3          →  Jump to Interaction Controls section
Alt+4          →  Jump to Motion & Sensory Controls section
Alt+5          →  Jump to Advanced Controls section

Help & Menus:
?              →  Show help/keyboard shortcuts
/              →  Search (future feature)
```

---

## 9. Testing Strategy (Accessibility-Focused)

### 9.1 Unit Tests Per Component

**Example: `FontSizeControl.test.tsx`**
```typescript
describe('FontSizeControl', () => {
  it('should apply font-size CSS to document', () => {
    const { getByRole } = render(<FontSizeControl />);
    const slider = getByRole('slider', { name: /font size/i });
    fireEvent.change(slider, { target: { value: 24 } });
    expect(document.body.style.fontSize).toBe('24px');
  });

  it('should persist to localStorage', () => {
    const { getByRole } = render(<FontSizeControl />);
    const slider = getByRole('slider', { name: /font size/i });
    fireEvent.change(slider, { target: { value: 24 } });
    expect(localStorage.getItem('fontSize')).toBe('24');
  });

  it('should have proper ARIA labels', () => {
    const { getByRole } = render(<FontSizeControl />);
    const slider = getByRole('slider');
    expect(slider).toHaveAttribute('aria-label');
    expect(slider).toHaveAttribute('aria-valuemin', '12');
    expect(slider).toHaveAttribute('aria-valuemax', '32');
  });
});
```

### 9.2 Keyboard Navigation Tests

```typescript
describe('Keyboard Navigation', () => {
  it('should tab through all controls in order', () => {
    const { container } = render(<AccessibilityPanel />);
    const interactiveElements = container.querySelectorAll(
      'button, [role="slider"], input[type="checkbox"]'
    );
    expect(interactiveElements.length).toBeGreaterThan(5);
    
    // Navigate and verify focus order
    for (let i = 0; i < interactiveElements.length; i++) {
      fireEvent.keyDown(document.body, { key: 'Tab' });
      expect(document.activeElement).toBe(interactiveElements[i]);
    }
  });

  it('should handle escape key to close modals', () => {
    const { getByRole, queryByRole } = render(<AccessibilityPanel />);
    const settingsButton = getByRole('button', { name: /settings/i });
    fireEvent.click(settingsButton);
    expect(queryByRole('dialog')).toBeInTheDocument();
    
    fireEvent.keyDown(document.body, { key: 'Escape' });
    expect(queryByRole('dialog')).not.toBeInTheDocument();
  });

  it('should support shortcut key R for Read Aloud', () => {
    const mockReadAloud = jest.fn();
    const { container } = render(
      <ReadAloudButton onRead={mockReadAloud} />
    );
    fireEvent.keyDown(document.body, { key: 'r', code: 'KeyR' });
    expect(mockReadAloud).toHaveBeenCalled();
  });
});
```

### 9.3 Screen Reader Compatibility Tests

```typescript
describe('Screen Reader Compatibility', () => {
  it('should have semantic HTML (button tags, not divs)', () => {
    const { getByRole } = render(<AccessibilityPanel />);
    expect(() => getByRole('button', { name: /read aloud/i })).not.toThrow();
  });

  it('should have ARIA labels on all controls', () => {
    const { container } = render(<AccessibilityPanel />);
    const interactiveElements = container.querySelectorAll(
      'button, [role="slider"], input'
    );
    interactiveElements.forEach((el) => {
      const hasLabel = 
        el.getAttribute('aria-label') ||
        el.getAttribute('aria-labelledby') ||
        el.textContent.trim();
      expect(hasLabel).toBeTruthy();
    });
  });

  it('should announce live changes with aria-live', () => {
    const { getByRole } = render(<SimplifiedTextOutput text="New text" />);
    const output = getByRole('region', { name: /simplified text/i });
    expect(output).toHaveAttribute('aria-live', 'polite');
  });

  it('should use aria-label for icon buttons', () => {
    const { getByRole } = render(<ReadAloudButton />);
    const button = getByRole('button');
    expect(button).toHaveAttribute('aria-label');
  });
});
```

### 9.4 Color Contrast Tests

```typescript
describe('Color Contrast Compliance (WCAG AA)', () => {
  it('should meet WCAG AA contrast ratio (4.5:1 for normal text)', () => {
    const { getByText } = render(
      <div style={{ color: '#000000', backgroundColor: '#FFFFFF' }}>
        Sample text
      </div>
    );
    const element = getByText('Sample text');
    const contrast = getContrast(
      getRGBFromElement(element),
      getRGBFromElement(element.parentElement)
    );
    expect(contrast).toBeGreaterThanOrEqual(4.5);
  });

  it('should maintain contrast in high contrast mode', () => {
    const { container } = render(
      <MainContent contrastMode={true} />
    );
    const textElements = container.querySelectorAll('p, span, button');
    textElements.forEach((el) => {
      const contrast = getContrast(
        getRGBFromElement(el),
        getRGBFromElement(el.parentElement)
      );
      expect(contrast).toBeGreaterThanOrEqual(7); // AAA level
    });
  });
});
```

### 9.5 User Persona Flow Tests

```typescript
describe('User Persona: Dyslexia', () => {
  it('should support full dyslexia-friendly workflow', () => {
    const { getByRole, getByLabelText } = render(<App />);
    
    // 1. Enable OpenDyslexic font
    const fontSelector = getByLabelText(/font.*select/i);
    fireEvent.change(fontSelector, { target: { value: 'OpenDyslexic' } });
    expect(document.body.style.fontFamily).toContain('OpenDyslexic');
    
    // 2. Increase line spacing
    const lineSpacingSlider = getByLabelText(/line spacing/i);
    fireEvent.change(lineSpacingSlider, { target: { value: 2.0 } });
    expect(document.body.style.lineHeight).toBe('2em');
    
    // 3. Apply color overlay
    const colorPicker = getByLabelText(/color.*overlay/i);
    fireEvent.click(colorPicker);
    fireEvent.click(getByRole('option', { name: /blue/i }));
    
    // 4. Paste text and simplify
    const textarea = getByRole('textbox');
    fireEvent.change(textarea, { target: { value: 'Complex text...' } });
    const simplifyBtn = getByRole('button', { name: /simplify/i });
    fireEvent.click(simplifyBtn);
    
    // Verify simplified text appears with all accessibility settings applied
    expect(textarea.parentElement).toHaveStyle('font-family: OpenDyslexic');
    expect(textarea.parentElement).toHaveStyle('line-height: 2em');
  });
});

describe('User Persona: Motor Difficulty', () => {
  it('should support keyboard-only workflow without mouse', () => {
    const { getByRole, container } = render(<App />);
    
    // Navigate entirely via keyboard
    fireEvent.keyDown(document.body, { key: 'Tab' });
    let focused = document.activeElement;
    expect(focused.tagName).toBe('BUTTON'); // Should focus buttons, not divs
    
    // Use keyboard shortcut D to dictate
    fireEvent.keyDown(document.body, { key: 'd', code: 'KeyD' });
    expect(container.querySelector('[aria-label*="Recording"]')).toBeInTheDocument();
    
    // Use Enter to submit (no mouse clicks needed)
    fireEvent.keyDown(focused, { key: 'Enter' });
  });
});

describe('User Persona: Visual Impairment', () => {
  it('should work entirely with screen reader', () => {
    const { getByLabelText, getByRole } = render(<App />);
    
    // Screen reader can find everything via ARIA labels
    const fontSizeControl = getByLabelText(/font size/i);
    expect(fontSizeControl).toBeInTheDocument();
    
    const readAloudButton = getByRole('button', { name: /read aloud/i });
    fireEvent.click(readAloudButton);
    
    // ARIA live region should announce
    expect(getByRole('status')).toHaveAttribute('aria-live', 'polite');
  });
});

describe('User Persona: ADHD', () => {
  it('should support guided mode for step-by-step workflow', () => {
    const { getByRole, getByText } = render(<App />);
    
    // Enable guided mode
    const guidedToggle = getByRole('checkbox', { name: /guided mode/i });
    fireEvent.click(guidedToggle);
    
    // Step 1: Only input visible
    expect(getByText(/step 1 of 4/i)).toBeInTheDocument();
    expect(getByRole('textbox')).toBeVisible();
    expect(getByRole('button', { name: /simplify/i })).toBeDisabled(); // Can't skip ahead
    
    // Paste text, move to Step 2
    fireEvent.change(getByRole('textbox'), { target: { value: 'Text...' } });
    const nextButton = getByRole('button', { name: /next/i });
    fireEvent.click(nextButton);
    
    // Step 2: Only simplify button active
    expect(getByText(/step 2 of 4/i)).toBeInTheDocument();
  });
});
```

### 9.6 Mobile Accessibility Tests

```typescript
describe('Mobile Accessibility', () => {
  it('should have min 48x48px touch targets', () => {
    const { getByRole } = render(<AccessibilityPanel />);
    const buttons = getByRole('button');
    
    buttons.forEach((btn) => {
      const { width, height } = btn.getBoundingClientRect();
      expect(width).toBeGreaterThanOrEqual(48);
      expect(height).toBeGreaterThanOrEqual(48);
    });
  });

  it('should be usable at 200% zoom (responsive)', () => {
    document.documentElement.style.zoom = '2';
    const { container } = render(<App />);
    expect(container.querySelector('main')).toBeInTheDocument();
    expect(container.querySelector('aside')).toBeInTheDocument();
    document.documentElement.style.zoom = '1';
  });
});
```

---

## 10. User Persona Example Flows

### Flow 1: User with Dyslexia

```
Timeline: ~5 minutes

1. Open AAI app
2. Panel visible on left with controls
3. User selects:
   - Font: "OpenDyslexic"
   - Line Spacing: 2.5x
   - Color Overlay: "Light Blue"
   - Enable: "Simplify Text"
4. User pastes article text
5. Click "Simplify This Text"
6. Simplified text appears with all settings applied
7. User clicks "Read Aloud"
8. Text plays while words highlight one-by-one
9. User can slow down speech (0.5x) if needed
10. User can dictate response using "Dictate" button
11. Settings auto-save to localStorage

Outcome: Dyslexic reader gets simplified, formatted text with audio support ✓
```

---

### Flow 2: User with Motor Difficulty (Severe)

```
Timeline: ~5 minutes

1. Open AAI app
2. User cannot use mouse (paralysis, tremors)
3. Uses Tab key to navigate controls
4. Uses keyboard shortcut D to start dictation
5. Speaks text that they want to simplify
6. Text auto-filled in textarea
7. Tab to "Simplify" button
8. Press Enter to activate
9. Simplified text appears
10. Press R to read aloud
11. Can't click "Speed" button, but Alt+S works (custom shortcut)

Perfect: Zero mouse required, only keyboard/voice ✓
```

---

### Flow 3: User with ADHD

```
Timeline: ~7 minutes

1. Open AAI app
2. Immediately overwhelmed by all controls
3. Finds toggle: "Guided Mode" → Enable
4. Interface transforms:
   - Sidebar hidden (too many controls)
   - Only main content visible
   - Step indicator: "Step 1 of 4: Paste Text"
5. Large, obvious textarea with placeholder
6. User pastes article
7. "Next" button appears at bottom
8. Click Next → Step 2
9. Only "Simplify" button visible, everything else grayed out
10. Click Simplify → Waits (progress bar instead of animation)
11. Step 3: Review simplified text (no jumping around)
12. Step 4: Choose action (Read / Copy / Download)
13. All steps locked until complete

Outcome: ADHD user completes task without distraction ✓
```

---

### Flow 4: Deaf User

```
Timeline: ~6 minutes

1. Open AAI app
2. Paste article text
3. Toggle: "Show Avatar" → Enable
4. Click "Simplify"
5. Simplified text appears
6. Sign Language Avatar animates below text
7. Avatar performs ASL translation of simplified text
8. Scrolls through animation in sync with text
9. User can toggle avatar off if wanted
10. Settings persist

Outcome: Deaf user sees sign language translation ✓
```

---

## 11. Color Palette (High Contrast & Theme Aware)

### Light Mode (Default)
```css
--bg-primary: #FFFFFF;
--bg-secondary: #F5F5F5;
--text-primary: #000000;
--text-secondary: #666666;
--border-color: #D0D0D0;
--accent-color: #0066CC;
--success-color: #008000;
--error-color: #DD0000;
--focus-ring: #0066CC;
--focus-ring-width: 3px;
```

### Dark Mode
```css
--bg-primary: #1a1a1a;
--bg-secondary: #2d2d2d;
--text-primary: #FFFFFF;
--text-secondary: #CCCCCC;
--border-color: #444444;
--accent-color: #66B3FF;
--success-color: #00CC00;
--error-color: #FF6666;
--focus-ring: #66B3FF;
```

### High Contrast Mode
```css
--bg-primary: #FFFFFF;
--bg-secondary: #FFFFFF;
--text-primary: #000000;
--text-secondary: #000000;
--border-color: #000000;
--accent-color: #0000FF;
--success-color: #000000 (with thick border);
--error-color: #FF0000;
--focus-ring: #0000FF;
--focus-ring-width: 4px;
```

---

## 12. Responsive Breakpoints

```css
/* Mobile First */
@media (max-width: 480px) {
  aside { width: 100%; height: auto; position: relative; }
  main { margin-left: 0; }
  .sidebar-toggle { display: block; }
}

@media (min-width: 481px) and (max-width: 768px) {
  aside { width: 60%; }
  main { margin-left: 60%; }
}

@media (min-width: 769px) {
  aside { width: 300px; }
  main { margin-left: 300px; }
}

@media (min-width: 1200px) {
  aside { width: 350px; }
  main { margin-left: 350px; }
}
```

---

## 13. Success Criteria (Accessibility Per User Type)

| User Type | Feature | Success Metric |
|-----------|---------|---|
| **Dyslexia** | OpenDyslexic + spacing + overlay | Font applied, spacing observable, colors persist |
| **ADHD** | Guided mode + reduced clutter | Wizard completes, < 2 sec per step, no distractions |
| **Visual** | Font size + contrast + screen reader | 32px readable, 7:1 contrast ratio, ARIA complete |
| **Auditory** | Avatar + captions | Avatar animates, sync with text |
| **Motor** | Keyboard-only + speech I/O | Tab navigation full, R/D shortcuts work, no mouse needed |
| **Neurodiverse** | Animations off + predictable layout | Zero motion, layout consistent, instant feedback |

All features tested per persona. 80%+ coverage required.

---

## 14. Implementation Checklist

### Phase 1: Foundation
- [ ] React project initialized with TypeScript
- [ ] Sidebar fixed layout (CSS grid)
- [ ] ARIA labels + semantic HTML on all controls
- [ ] Tab navigation working
- [ ] localStorage integration proven
- [ ] CSS variables set up (themes, colors, spacing)

### Phase 2: Dyslexia Features
- [ ] Font selector dropdown (OpenDyslexic loaded)
- [ ] Line spacing slider (1-3x)
- [ ] Letter spacing slider (0-2px)
- [ ] Color overlay picker (5 colors)
- [ ] All settings persist to localStorage

### Phase 3: Visual Adjustments
- [ ] Font size control (12-32px)
- [ ] High contrast mode toggle
- [ ] Dark/light mode switcher
- [ ] Focus indicators (3px outline on all interactive elements)
- [ ] Color contrast ratio ≥ 4.5:1 (WCAG AA)

### Phase 4: Motion & ADHD Support
- [ ] Reduce motion toggle (CSS + JS)
- [ ] Guided mode wizard (4 steps)
- [ ] Minimal mode toggle
- [ ] disable auto-play + animations

### Phase 5: Speech & Interaction
- [ ] Read aloud button (Web Speech API)
- [ ] Word-by-word highlighting during speech
- [ ] Dictate button (STT)
- [ ] Speech rate control (0.5-2x)

### Phase 6: Avatar & Advanced
- [ ] Sign language avatar component
- [ ] Avatar toggle in settings
- [ ] Avatar animation library integration

### Phase 7: Testing
- [ ] Unit tests for all controls (80%+ coverage)
- [ ] Keyboard navigation tests
- [ ] Screen reader tests (ARIA validation)
- [ ] Color contrast tests (automated)
- [ ] User persona flow tests (6 flows)
- [ ] Mobile accessibility tests (48px targets)

---

## 15. Deployment Checklist

Before deploying to Vercel:

- [ ] All accessibility controls functional
- [ ] localStorage persistence working
- [ ] No console errors
- [ ] Mobile responsive (tested on 480px, 768px, 1024px widths)
- [ ] WCAG AA compliance verified (axe DevTools)
- [ ] Screen reader tested (NVDA or JAWS simulation)
- [ ] Lighthouse accessibility score ≥ 90
- [ ] Performance score ≥ 85
- [ ] All UAT tests passing (5 scenarios from UAT_PLAN.md)

---

## 16. Future Enhancements (Post-MVP)

1. **Behavioral Adaptation:** Learn user preferences over time
2. **Cognitive Load Detection:** Monitor user stress indicators
3. **Personalized Templates:** Save custom control combinations
4. **Multi-language Support:** i18n for global accessibility
5. **Browser Extension:** Embed AAI in any website
6. **Analytics Dashboard:** Track feature usage per persona
7. **A/B Testing:** Test control layouts, wording, colors
8. **Integration APIs:** Embed AAI in third-party apps
9. **Real-time Collaboration:** Multiple users with shared simplified text
10. **AI Avatar Improvements:** 3D avatars, more sign languages, custom animations

---

## Summary Table: Features Mapping

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│ Accessibility Need → Frontend Feature → Component → Backend API                    │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ Dyslexia              OpenDyslexic Font    FontSelector.tsx      (localStorage)    │
│                       Line Spacing         LineSpacingControl    (localStorage)    │
│                       Letter Spacing       LetterSpacingControl  (localStorage)    │
│                       Color Overlay        ColorOverlayPicker    (localStorage)    │
│                       Text Simplification  SimplifyButton        /api/text/simplify│
├─────────────────────────────────────────────────────────────────────────────────────┤
│ ADHD                  Minimal Mode         MinimalModeToggle     (localStorage)    │
│                       Guided Mode Wizard   GuidedModeWizard      (localStorage)    │
│                       Reduce Motion        ReduceMotionToggle    (localStorage)    │
│                       Clear Hierarchy      UI Design (CSS)       (N/A)             │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ Visual Impairment     Font Size            FontSizeControl       (localStorage)    │
│                       High Contrast        ContrastModeToggle    (localStorage)    │
│                       Dark Mode            ThemeToggle           (localStorage)    │
│                       Keyboard Navigation  FocusManager.tsx      (N/A)             │
│                       Screen Reader        ARIA labels + semantic HTML (N/A)       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ Auditory Impairment   Sign Language Avatar SignLanguageAvatar.tsx /api/avatar/sign │
│                       Captions             TranscriptionDisplay  (Web API)         │
│                       Visual Indicators    StatusBar.tsx         (N/A)             │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ Motor Difficulty      Keyboard-Only        KeyboardNavigation    (N/A)             │
│                       Speech-to-Text       DictateButton.tsx     (Web Speech API)  │
│                       Large Click Targets  CSS min-size 48x48    (N/A)             │
│                       Predictive Typing    AutoSuggestion.tsx    /api/text/predict │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ Neurodiverse          Reduced Animations   ReduceMotionToggle    (localStorage)    │
│                       Predictable Layout   Fixed sidebar         (CSS)             │
│                       Customization        AccessibilityPanel    (localStorage)    │
│                       Instant Feedback     UI state updates      (React state)     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

**Document Complete.** Ready for implementation.

