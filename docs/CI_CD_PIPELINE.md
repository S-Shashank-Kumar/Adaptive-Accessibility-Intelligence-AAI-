# CI/CD Pipeline – AAI (FastAPI + GitHub Actions)

## 1. Branch Strategy

main → Production  
develop → Staging  
feature/* → Feature branches  

---

## 2. CI Pipeline Stages

1. Install dependencies
2. Run flake8 (linting)
3. Run pytest (unit + integration tests)
4. Run bandit (security scan)
5. Run dependency vulnerability check
6. Build validation

---

## 3. Deployment Strategy

After merge to main:
- Backend deployed to Render or Railway
- Frontend deployed to Vercel

---

## 4. Merge Protection Rules

- Tests must pass
- Security scan must pass
- Code review required