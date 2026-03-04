# Security Architecture – AAI

## 1. Security Philosophy

- Least privilege principle
- Defense in depth
- Zero trust API boundaries
- Secure by default

---

## 2. Authentication & Authorization

- JWT-based authentication
- Access tokens expire in 30 minutes
- Future-ready for role-based access control

---

## 3. FastAPI-Specific Security Controls

- Pydantic request validation
- Dependency-based auth guards
- Automatic schema validation
- Debug mode disabled in production

---

## 4. API Security

- HTTPS only
- CORS restricted to trusted origins
- Rate limiting per IP
- Request size limits
- Input validation on all endpoints

---

## 5. Secure Headers

- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- Content-Security-Policy
- Strict-Transport-Security

---

## 6. Data Protection

- Passwords hashed using bcrypt
- API keys stored in environment variables
- Database credentials not committed
- Optional encryption at rest

---

## 7. Secrets Management

- .env file for local
- GitHub Secrets for CI
- No secrets in frontend code