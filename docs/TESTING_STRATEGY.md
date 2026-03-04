# Testing Strategy – AAI (FastAPI Edition)

## 1. Testing Levels

### Unit Tests
- Service layer logic
- Text simplification service
- Authentication logic
- Utility functions

Tools:
- Pytest
- Mocking via unittest.mock

---

### Integration Tests
- FastAPI TestClient
- API endpoint testing
- Backend-to-service flow validation

---

### Security Testing
- Invalid JWT validation
- SQL injection attempts
- XSS input validation

---

### UAT Testing
- Real user flows
- Accessibility scenario validation

---

## 2. Coverage Target

Minimum coverage: 80%

---

## 3. CI Enforcement

Tests must pass before merge into main branch.