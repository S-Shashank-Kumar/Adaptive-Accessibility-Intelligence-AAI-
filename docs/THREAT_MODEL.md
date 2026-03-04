# Threat Model – AAI

## 1. Assets

- User profile data
- JWT tokens
- AI API keys

---

## 2. Threats & Mitigations

### Injection Attacks
Mitigation:
- Pydantic validation
- SQLAlchemy ORM usage

---

### Cross-Site Scripting (XSS)
Mitigation:
- Sanitize HTML
- CSP headers

---

### API Abuse
Mitigation:
- Rate limiting
- Request validation

---

### Token Theft
Mitigation:
- HTTPS enforced
- Short-lived JWT tokens

---

## 3. Risk Assessment

MVP Risk Level: Medium  
Production deployment requires penetration testing.