# Phase 3 — Lesson 1: Feature Development Simulation

**Role:** Web Developer  
**Thời lượng:** 120–150 phút  
**Scenario:** Bạn nhận một feature mới từ Product Owner và phải đưa nó từ requirement đến Pull Request.

---

## 1. Context

Bạn đang làm việc trên một e-commerce application.

Product Owner tạo Jira ticket:

> **Add product search**

Requirement:

> Users should be able to search for products by name. The API should return matching products and support pagination.

---

## 2. Your First Task — Clarify the Requirement

Requirement còn thiếu một số thông tin.

Hãy viết ít nhất 6 câu hỏi bằng English.

Bạn cần hỏi về:

- search có case-sensitive không?
- search theo exact match hay partial match?
- page size mặc định là bao nhiêu?
- nếu không tìm thấy sản phẩm thì response thế nào?
- có cần sort không?
- search có hỗ trợ special characters không?

### Useful patterns

```text
Could you clarify...?
What should happen if...?
Should the API...?
Do we need to...?
Is ... supported?
What is the default...?
```

---

## 3. Product Owner Response

Product Owner trả lời:

> The search should be case-insensitive and support partial matches. The default page size is 20. If no products are found, the API should return an empty list. Results should be sorted by relevance.

### Task

Viết lại requirement bằng English rõ ràng hơn.

---

## 4. Technical Planning

Bạn cần đề xuất implementation.

Viết 5–8 câu English.

Gợi ý:

```text
I suggest...
The API will...
The database query should...
We need to...
The endpoint will...
```

Bạn cần đề cập:

- endpoint
- query parameter
- pagination
- sorting
- database query

---

## 5. Daily Standup

Viết một standup update:

```text
Yesterday:
Today:
Blocker:
```

---

## 6. Implementation Problem

Trong quá trình implement, bạn phát hiện database query khá chậm khi search trên một lượng lớn products.

Hãy mô tả vấn đề bằng English.

Dùng:

```text
The problem occurs when...
The query takes...
The main issue is...
I think we should...
```

---

## 7. Technical Discussion

Team hỏi:

> Should we add an index or introduce a search engine?

Viết câu trả lời 8–10 câu.

Phải có:

- recommendation
- advantage
- drawback
- trade-off
- conclusion

---

## 8. Pull Request

Viết PR description:

```text
## Summary

## What changed

## Why

## Testing

## Performance
```

---

## 9. Code Review

Reviewer:

> Could you add a test for an empty search result?

Bạn trả lời.

Reviewer tiếp:

> The query logic is quite complex. Could we simplify it?

Bạn trả lời 3–5 câu.

---

## 10. Final Developer Update

Viết một đoạn 5–7 câu:

> Feature completed → tests passed → PR approved → ready for staging.

---

## 11. Success Criteria

Bạn hoàn thành bài khi có thể tự viết:

- requirement clarification
- technical proposal
- standup
- problem description
- PR description
- code review response
- final update

mà không cần dịch từng câu từ tiếng Việt trong đầu.
