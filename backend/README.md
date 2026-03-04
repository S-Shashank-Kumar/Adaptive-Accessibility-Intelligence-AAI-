# AAI Backend

FastAPI backend for Adaptive Accessibility Intelligence platform.

## Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

### 4. Initialize Database
```bash
python -c "from app.database import init_db; init_db()"
```

### 5. Run Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server runs at: http://localhost:8000

### API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest app/tests/test_auth.py -v
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── config.py            # Settings
│   ├── database.py          # DB setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── dependencies.py      # Dependency injection
│   ├── routes/
│   │   ├── health.py       # Health check
│   │   ├── auth.py         # Authentication
│   │   ├── text.py         # Text simplification
│   │   └── user.py         # User profile
│   ├── services/
│   │   ├── auth.py         # Auth logic
│   │   └── text_adapter.py # NLP service
│   └── tests/
│       ├── conftest.py     # Test config
│       ├── test_auth.py
│       ├── test_text.py
│       └── test_user.py
├── requirements.txt
├── .env.example
└── README.md
```

## API Endpoints

### Health
- `GET /api/v1/health` - Health check

### Authentication
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login and get JWT token

### User
- `GET /api/v1/user/profile` - Get accessibility profile
- `PUT /api/v1/user/profile` - Update accessibility profile

### Text
- `POST /api/v1/text/simplify` - Simplify text

## Security

- Passwords hashed with bcrypt
- JWT tokens expire in 30 minutes
- All inputs validated with Pydantic
- CORS restricted to trusted origins
