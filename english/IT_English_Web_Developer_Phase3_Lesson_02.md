# Phase 3 — Lesson 2: Authentication Feature Simulation

**Thời lượng:** 120–150 phút

## Scenario

Team yêu cầu:

> **Implement user login API**

Requirement:

> Users should be able to log in with an email address and password. The API should return an access token after successful authentication.

---

## 1. Clarify

Đặt ít nhất 6 câu hỏi về:

- password validation
- invalid credentials
- token expiration
- refresh token
- account status
- rate limiting

---

## 2. Product Owner Response

> The API should return a generic error for invalid credentials. Access tokens expire after 30 minutes. Refresh tokens are required. Locked accounts cannot log in.

### Task

Viết lại requirement bằng English.

---

## 3. Technical Plan

Mô tả implementation:

```text
POST /api/login
```

Request:

```json
{
  "email": "user@example.com",
  "password": "..."
}
```

Viết 8–10 câu English mô tả:

- validation
- authentication
- token generation
- error handling
- security

---

## 4. Standup

Viết update:

```text
Yesterday:
Today:
Blocker:
```

---

## 5. Production-like Bug

Trong quá trình testing:

> Some users receive a 500 error when they enter an incorrect password.

Hãy viết:

```text
Expected behavior:
Actual behavior:
Steps to reproduce:
Possible root cause:
Impact:
```

---

## 6. Technical Discussion

Team hỏi:

> Should we return a detailed error message?

Giải thích tại sao bạn chọn generic error hoặc detailed error.

Dùng:

```text
From a security perspective...
I think we should...
The main risk is...
```

---

## 7. Pull Request

Viết PR description cho login API.

---

## 8. Code Review

Reviewer:

> Why do we generate a refresh token instead of asking the user to log in again?

Trả lời bằng 5–7 câu.

Reviewer:

> Please add tests for locked accounts.

Trả lời và mô tả bạn đã xử lý.

---

## 9. Final Update

Viết một update cho team:

> Authentication API completed → tests added → security issue fixed → PR ready.

---

## Success Criteria

Bạn phải có thể giải thích bằng English:

**How does your login API work?**

trong khoảng 1–2 phút.
