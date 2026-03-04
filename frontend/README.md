# AAI Frontend

React frontend for Adaptive Accessibility Intelligence platform.

## Setup

### 1. Install Dependencies
```bash
npm install
```

### 2. Configure Environment
Create `.env` file:
```
REACT_APP_API_URL=http://localhost:8000/api/v1
```

### 3. Run Development Server
```bash
npm start
```

Server runs at: http://localhost:3000

### 4. Build for Production
```bash
npm run build
```

## Testing

```bash
npm test

# With coverage
npm test -- --coverage
```

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── AccessibilityPanel/
│   │   │   └── AccessibilityPanel.tsx
│   │   └── MainContent/
│   │       └── MainContent.tsx
│   ├── hooks/
│   │   └── useAccessibilitySettings.tsx
│   ├── services/
│   │   └── api.ts
│   ├── styles/
│   │   └── index.css
│   ├── types/
│   │   └── accessibility.ts
│   ├── App.tsx
│   └── index.tsx
├── public/
│   └── index.html
├── package.json
├── tsconfig.json
└── README.md
```

## Features

### Accessibility Controls
- Font size adjustment (12px-32px)
- Line spacing control (1.0x-3.0x)
- Letter spacing control (0px-2px)
- Dyslexia-friendly font selector
- Color overlay options
- High contrast mode
- Dark/light mode
- Reduce motion/animation
- Sound toggle
- Vibration toggle
- Minimal mode
- Guided mode
- Sign language avatar toggle

### Core Features
- Text simplification (NLP-powered)
- Read aloud (Web Speech API TTS)
- Dictate (Web Speech API STT)
- User authentication (JWT)
- Settings persistence (localStorage)

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Keyboard Shortcuts

- `R` - Read aloud
- `D` - Dictate
- `S` - Simplify text

## Accessibility

- WCAG 2.1 AA compliant
- Full keyboard navigation
- Screen reader support
- Semantic HTML
- Color contrast ratios ≥ 4.5:1
- 48x48px minimum touch targets
