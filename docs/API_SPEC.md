# API Specification – AAI (FastAPI)

Base Path: /api/v1

Auto-generated documentation:
- Swagger UI: /docs
- ReDoc: /redoc

---

## Authentication

POST /auth/login

Request:
{
  "email": "user@example.com",
  "password": "string"
}

Response:
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}

---

## Text Simplification

POST /text/simplify

Request:
{
  "text": "Complex paragraph",
  "reading_level": "basic"
}

Response:
{
  "simplified_text": "Simplified version..."
}

---

## User Profile

GET /user/profile

Headers:
Authorization: Bearer <token>

Response:
{
  "font_size": "large",
  "contrast_mode": true
}

---

## Health Check

GET /health

Response:
{
  "status": "ok"
}