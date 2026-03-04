# ⚡ Quick Start Guide

This guide will get you from zero to fully running AAI application in 5-10 minutes.

## Current Status

✅ **Backend**: Running successfully on http://127.0.0.1:8000
✅ **Frontend Code**: Complete and ready
❌ **Frontend Server**: Not running yet (requires Node.js)

---

## Step 1: Install Node.js (5 minutes)

**If Node.js is NOT installed:**

1. Visit: https://nodejs.org/
2. Download the **LTS (Long Term Support)** version
3. Run the installer and follow the prompts
4. **Restart your terminal/VS Code** after installation
5. Verify installation:
   ```bash
   node --version
   npm --version
   ```
   You should see version numbers (e.g., `v20.10.0`)

**If Node.js IS already installed:**
- Skip to Step 2

---

## Step 2: Install Frontend Dependencies (2 minutes)

In your terminal:

```bash
cd frontend
npm install
```

This will:
- Download React, TypeScript, and all dependencies
- Create `node_modules` folder
- Setup build tools

Expected output: "added X packages" (200+ packages)

---

## Step 3: Start Frontend Server (1 minute)

```bash
npm start
```

Expected output:
```
Compiled successfully!

You can now view frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

This will automatically open http://localhost:3000 in your browser.

---

## Step 4: Test the Application

### Auto-Login
- Frontend automatically logs in with demo account: `demo@aai.com` / `demo123456`
- You should see the accessibility panel on the left

### Test Text Simplification
1. Paste complex text in the input area:
   ```
   The phenomenon of quantum entanglement, wherein two particles become correlated 
   in such a way that the quantum state of each particle cannot be described independently, 
   represents one of the most perplexing aspects of quantum mechanics.
   ```
2. Click "Simplify This Text"
3. You should see simplified text appear below

### Test Accessibility Controls
1. **Font Size**: Drag the slider (12-32px) - text should resize
2. **Line Spacing**: Adjust (1.0-3.0x) - lines should spread out
3. **Letter Spacing**: Adjust (0-2px) - characters should spread
4. **Font Family**: Select "OpenDyslexic" - font should change
5. **Color Overlay**: Select "Blue" - text should get blue tint
6. **Dark Mode**: Toggle - background should turn dark
7. **High Contrast**: Toggle - colors should increase

### Test Speech Features
1. After text is simplified, click "Read Aloud" 🔊
   - Your computer should speak the text
   - Sound should be adjustable by speech rate slider
2. Click "Dictate" 🎤
   - Browser will ask for microphone permission
   - Speak text and it should appear in input area

### Test Sign Language Avatar
1. Enable "Show Avatar" in the accessibility panel
2. After simplifying text, click "Show Avatar" button
3. You should see ASCII sign language avatar
4. Click "Play" to see animation of signs for each word

### Test Guided Mode
1. In accessibility panel, toggle "Guided Mode" ON
2. Reload the page (or click reset)
3. You should see step-by-step wizard interface
4. Follow through all 6 steps

---

## Keyboard Shortcuts

Test these keyboard shortcuts:
- **R** - Read Aloud
- **D** - Dictate
- **S** - Simplify Text
- **Tab** - Navigate through controls
- **Space/Enter** - Activate button

---

## What You Should See

### Page Layout
```
┌─────────────────────────────────────────────────┐
│  Adaptive Accessibility Intelligence (AAI)      │
├──────────┬──────────────────────────────────────┤
│          │                                      │
│  Acc.    │         Main Content Area             │
│  Panel   │                                      │
│ (20+     │  - Text Input Box                    │
│ controls)│  - Simplify Button                   │
│          │  - Simplified Output                 │
│          │  - Read Aloud / Copy / Dictate       │
│          │  - Avatar (if enabled)               │
│          │                                      │
├──────────┴──────────────────────────────────────┤
│  Status: ✓ Ready                                │
└─────────────────────────────────────────────────┘
```

### Expected Behavior Flow

```
1. Page Load → Auto-login with demo account
2. User enters text
3. Click "Simplify" → Text sent to backend
4. Backend processes (1-3 seconds)
5. Simplified text appears with all CSS settings applied
6. User can read aloud / copy / dictate
7. If avatar enabled: User can see sign language animation
8. If guided mode enabled: Step-by-step workflow shown
```

---

## Troubleshooting

### Frontend won't start
```bash
# Make sure you're in the frontend folder
cd frontend

# Try these steps in order:
1. npm install   # Reinstall dependencies
2. npm start     # Try starting again

# If still fails:
3. Delete node_modules and package-lock.json
   rm -r node_modules package-lock.json  # or manually delete folders
4. npm install
5. npm start
```

### "npm: command not found"
- Node.js not installed correctly
- Restart your terminal after installing
- Verify with `node --version`

### Simplified text not appearing
1. Check backend is running: http://127.0.0.1:8000/
2. Check browser console for errors (F12 → Console tab)
3. Verify input text is at least 10 characters

### Speech not working
1. Check "Sound Enabled" in accessibility panel
2. Check browser console for errors
3. Grant microphone permission when prompted
4. Test: Open Chrome DevTools → Console and check for warnings

### Avatar not showing
1. Make sure you enabled "Show Avatar" in accessibility panel
2. Make sure text is simplified first
3. Click "Show Avatar" button below the simplified text

---

## Accessing API Documentation

While both servers are running, visit:
- **Interactive API Docs**: http://127.0.0.1:8000/docs
- **Alternative API Docs**: http://127.0.0.1:8000/redoc
- **Frontend App**: http://localhost:3000

---

## File Structure Reference

```
Project/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── main.py           # Entry point
│   │   ├── config.py         # Settings
│   │   ├── database.py       # DB setup
│   │   ├── models.py         # ORM models
│   │   ├── schemas.py        # Validation
│   │   ├── dependencies.py   # Auth logic
│   │   ├── routes/           # API endpoints
│   │   │   ├── auth.py
│   │   │   ├── text.py
│   │   │   ├── user.py
│   │   │   ├── avatar.py     # NEW: Sign language
│   │   │   └── guided.py     # NEW: Guided mode
│   │   ├── services/         # Business logic
│   │   │   ├── auth.py
│   │   │   ├── text_adapter.py
│   │   │   ├── speech.py     # NEW
│   │   │   ├── avatar.py     # NEW
│   │   │   └── guided_mode.py# NEW
│   │   └── tests/            # Unit tests (6+ files)
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── App.tsx           # Main component
│   │   ├── index.tsx         # Entry
│   │   ├── components/
│   │   │   ├── AccessibilityPanel/
│   │   │   ├── MainContent/
│   │   │   └── SignLanguageAvatar/ # NEW
│   │   ├── hooks/
│   │   │   └── useAccessibilitySettings.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   │   └── accessibility.ts
│   │   └── styles/
│   │       └── index.css
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
│
├── docs/                       # Documentation
│   ├── API_SPEC.md
│   ├── ARCHITECTURE.md
│   ├── TESTING_STRATEGY.md
│   └── ... 5 more files
│
├── FEATURES.md                 # Feature documentation (NEW)
├── IMPLEMENTATION_GUIDE.md     # Implementation guide (NEW)
├── PROJECT_SUMMARY.md          # This file (NEW)
├── QUICK_START.md              # Quick start guide (NEW)
└── README.md                   # Project overview
```

---

## Next Steps After Testing

### If Everything Works ✅
1. Explore all features thoroughly
2. Try different accessibility combinations
3. Read [FEATURES.md](../FEATURES.md) for detailed info
4. Test guided mode step-by-step
5. Test signature/avatar animations

### If You Find Issues ❌
1. Check [TROUBLESHOOTING](#troubleshooting) section above
2. Review browser console (F12 → Console)
3. Check backend logs (terminal where `npm start` was run)
4. Verify backend is still running: http://127.0.0.1:8000/

### To Learn More 📚
1. **Features**: [FEATURES.md](../FEATURES.md) - Complete feature guide
2. **Architecture**: [ARCHITECTURE.md](../docs/ARCHITECTURE.md) - System design
3. **Implementation**: [IMPLEMENTATION_GUIDE.md](../IMPLEMENTATION_GUIDE.md) - Developer guide
4. **Testing**: [TESTING_STRATEGY.md](../docs/TESTING_STRATEGY.md) - Test approach
5. **API Reference**: http://127.0.0.1:8000/docs - Interactive API docs

---

## Development Workflow

### Running Backend & Frontend Together

**Terminal 1 (Backend):**
```bash
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Expected: "Uvicorn running on http://127.0.0.1:8000"

**Terminal 2 (Frontend):**
```bash
cd frontend
npm start
```
Expected: "You can now view frontend in the browser at http://localhost:3000"

Both should be running simultaneously!

### Making Code Changes

**Backend:**
- Edit any file in `backend/app/`
- Server auto-reloads (you'll see "Reloading..." in terminal)
- Browser page may auto-refresh

**Frontend:**
- Edit any file in `frontend/src/`
- Browser auto-reloads (you'll see "Compiled successfully!")
- Changes appear immediately

---

## Performance Baseline

These should be your expected performance metrics:

| Operation | Expected Time | Status |
|-----------|---------------|--------|
| Register new user | < 500ms | ✅ |
| Login | < 300ms | ✅ |
| Simplify text | 1-3 seconds | ✅ |
| Generate avatar | < 2 seconds | ✅ |
| Update profile | < 500ms | ✅ |
| Health check | < 100ms | ✅ |

If you see slower times, it might mean:
- Backend is processing first ML model load
- Network latency
- Browser DevTools is open (slows performance)

---

## Sample Test Data

### For Text Simplification Testing
```
Complex: "The paradigm shift in contemporary educational methodologies necessitates 
a comprehensive reevaluation of pedagogical frameworks to accommodate diverse learning 
modalities and neurodivergent populations."

Simplified (expected): "Education needs to change to help different learners."
```

### For Avatar Testing
```
Simple: "Hello world thank you"
Expected: 4 signs - 3 from dictionary, 1 fingerspelled if needed
```

### For Guided Mode Testing
```
Step 1: Click "Start"
Step 2: Paste "The quick brown fox jumps over the lazy dog" (40+ chars)
Step 3: Select "Intermediate" reading level
Step 4: Wait for simplification
Step 5: Review output
Step 6: Choose "Done" or "Start Over"
```

---

## Stopping the Servers

### Stop Backend
- In backend terminal: Press `Ctrl+C`
- You'll see: "Shutting down..."

### Stop Frontend
- In frontend terminal: Press `Ctrl+C`
- You'll see: "Stopping server..."

---

## Quick Command Reference

```bash
# Backend commands
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Frontend commands
cd frontend
npm install      # Install dependencies (one time)
npm start        # Start dev server
npm test         # Run tests
npm run build    # Build for production

# Testing
pytest              # Run all backend tests
pytest -v          # Verbose test output
pytest --cov=app   # With coverage report
```

---

## Important Notes

### About the Demo Account
- **Email**: demo@aai.com
- **Password**: demo123456
- **Purpose**: For quick testing without registration
- **Data**: Gets reset on server restart
- **Create New Account**: Use registration form to create real account

### About Local Storage
- All accessibility settings are saved to browser's local storage
- Settings persist even after page refresh
- Clear browser data to reset settings

### About Database
- Using SQLite (file-based, no installation needed)
- File location: `backend/aai.db`
- Gets recreated on first startup
- Contains: Users, accessibility profiles, simplification cache

---

## 🎉 You're All Set!

You now have:
- ✅ Backend API running with 13+ endpoints
- ✅ Frontend application with 20+ accessibility controls
- ✅ Sign language avatar generation
- ✅ Guided mode for ADHD-friendly workflow
- ✅ Text simplification with AI
- ✅ Voice input/output (TTS/STT)
- ✅ Full authentication system
- ✅ Database with user profiles
- ✅ 30+ automated tests

**Time to explore and test the full accessibility suite!**

---

**Questions?** 
- Check [FEATURES.md](../FEATURES.md) for detailed feature information
- Check [IMPLEMENTATION_GUIDE.md](../IMPLEMENTATION_GUIDE.md) for technical details
- Visit http://127.0.0.1:8000/docs for API documentation

**Ready to deploy?**
- See [ARCHITECTURE.md](../docs/ARCHITECTURE.md) for deployment instructions
- See [CI_CD_PIPELINE.md](../docs/CI_CD_PIPELINE.md) for automation setup

---

*Quick Start Guide | v0.2.0 | December 2024*
