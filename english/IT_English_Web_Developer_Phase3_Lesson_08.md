# Phase 3 — Lesson 8: Full Web Developer Simulation

**Thời lượng:** 180 phút

# Scenario

Bạn là Web Developer trong một e-commerce team.

Product Owner tạo Jira:

> **Add Order Cancellation**

Requirement:

> Users should be able to cancel an order before it is shipped.

---

# Part 1 — Clarify Requirement

Viết ít nhất 8 câu hỏi.

Cần hỏi:

- order status
- cancellation deadline
- payment refund
- partial cancellation
- API response
- authorization
- edge cases
- audit log

---

# Part 2 — Requirement

Sau khi trao đổi, requirement được xác nhận:

> Users can cancel an order while its status is `PENDING` or `CONFIRMED`. Orders that have already been shipped cannot be cancelled. A successful cancellation triggers a refund process.

Viết lại requirement thành technical specification ngắn.

---

# Part 3 — Technical Design

Bạn cần mô tả:

```text
API
Database
Business logic
Authorization
Refund
Error handling
```

Viết 10–15 câu English.

---

# Part 4 — Daily Standup

Viết:

```text
Yesterday:
Today:
Blocker:
```

---

# Part 5 — Implementation

Trong quá trình coding, bạn phát hiện:

> The refund service is asynchronous.

Giải thích bằng English cách bạn sẽ xử lý.

Dùng:

```text
event
queue
background job
retry
failure
status
```

---

# Part 6 — Bug

QA report:

> The API allows a user to cancel an order that belongs to another user.

Viết:

```text
Expected behavior:
Actual behavior:
Impact:
Root cause:
Fix:
Regression test:
```

---

# Part 7 — Technical Discussion

Team hỏi:

> Should authorization happen in the controller or service layer?

Trình bày quan điểm.

Phải có:

```text
I think...
One advantage...
One drawback...
From a maintainability perspective...
I would recommend...
```

---

# Part 8 — Pull Request

Viết PR description:

```text
## Summary

## Technical changes

## Security

## Testing

## Risks

## Deployment notes
```

---

# Part 9 — Code Review

Reviewer:

> The cancellation logic is getting too complex.

Trả lời.

Reviewer:

> Please add a test for cross-user access.

Trả lời.

Reviewer:

> Why is the refund handled asynchronously?

Trả lời.

---

# Part 10 — Deployment

Bạn deploy lên staging.

QA báo:

> Cancellation works, but refund processing is delayed.

Viết update cho team.

---

# Part 11 — Production

Sau production deployment:

```text
Cancellation API: healthy
Refund queue: healthy
Error rate: normal
```

Viết release update.

---

# Part 12 — Documentation

Viết một technical note:

> **Order Cancellation API**

Phải có:

```text
Purpose
Endpoint
Request
Response
Authorization
Business rules
Error cases
Examples
```

---

# Final Challenge

Không dùng translator.

Hãy hoàn thành toàn bộ workflow bằng English:

```text
Requirement
    ↓
Clarification
    ↓
Technical Design
    ↓
Standup
    ↓
Implementation
    ↓
Bug
    ↓
Technical Discussion
    ↓
Pull Request
    ↓
Code Review
    ↓
Deployment
    ↓
Documentation
```

## Phase 3 Graduation Test

Bạn đạt mục tiêu Phase 3 nếu có thể:

1. Đọc một Jira ticket và hiểu yêu cầu.
2. Đặt câu hỏi clarification.
3. Giải thích solution.
4. Mô tả bug.
5. Viết PR.
6. Trả lời reviewer.
7. Thảo luận trade-off.
8. Viết deployment update.
9. Viết technical documentation.

### Final question

Viết 200–300 từ trả lời:

> **Describe how you would develop, test, review, and deploy a new feature in a web application.**

Không cần dùng từ quá khó.

Mục tiêu là **rõ ràng, chính xác và tự nhiên**.

---

# 80/20 Master Patterns

```text
Could you clarify...?
What should happen if...?
I think we should...
One possible approach is...
The main advantage is...
The main drawback is...
I see your point, but...
I have a concern about...
The issue occurs when...
We were able to reproduce...
The root cause is...
I've addressed your comments.
The fix has been deployed.
We decided to roll back...
The feature is ready for production.
```

# Final Goal

> **You are no longer translating English about software. You are using English to work on software.**
