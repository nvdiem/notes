# Phase 2 — Lesson 7: Technical Writing — Tickets, PRs & Documentation

**Thời lượng:** 120 phút

## 1. Writing Vocabulary

`overview`, `purpose`, `scope`, `implementation`, `configuration`, `usage`, `example`, `request`, `response`, `parameter`, `assumption`, `limitation`, `note`.

## 2. Technical Writing Patterns

> This document describes...

> The purpose of this endpoint is to...

> This API is used to...

> The endpoint accepts...

> The request must contain...

> The response contains...

> To use this feature,...

> The following example shows...

> Note that...

> This implementation does not support...

## 3. PR Description Template

```text
## Summary
Briefly describe the change.

## What changed
- ...
- ...
- ...

## Why
Explain the reason.

## Testing
Explain how you tested it.

## Notes
Mention limitations or risks.
```

## 4. Reading — PR Description

> This pull request adds support for password reset. Users can request a reset link by providing their email address.
>
> The API validates the email address and creates a temporary reset token. The token is sent to the user by email and expires after 30 minutes.
>
> The implementation includes validation tests and integration tests for the reset flow. The API returns a generic response when the email address does not exist to prevent user enumeration.

## 5. Translation

1. This document describes the authentication API.
2. The endpoint is used to reset a user's password.
3. The request must contain a valid email address.
4. The token expires after 30 minutes.
5. The implementation includes integration tests.
6. Note that the token can only be used once.
7. The API returns a generic response.
8. This feature does not support social login.

## 6. Reverse Translation

1. Tài liệu này mô tả authentication API.
2. Endpoint này được sử dụng để reset password.
3. Request phải chứa email hợp lệ.
4. Token hết hạn sau 30 phút.
5. Implementation bao gồm integration tests.
6. Lưu ý rằng token chỉ có thể được sử dụng một lần.
7. API trả về một response chung.

## 7. Practical Writing

Viết một PR description ngắn cho task:

> Add pagination to the users API.

Phải có:

```text
Summary
What changed
Why
Testing
Notes
```

**80/20:** `This document describes...` / `This API is used to...` / `The request must...` / `The response contains...` / `Note that...`
