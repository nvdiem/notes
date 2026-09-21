# Phase 2 — Lesson 8: End-to-End Workplace Communication

**Thời lượng:** 120–150 phút

## Mục tiêu

Kết hợp 7 bài trước vào một workflow thực tế:

```text
Jira ticket
→ clarify requirement
→ implement
→ daily standup
→ bug investigation
→ pull request
→ code review
→ technical discussion
→ documentation
```

---

# 1. Scenario

Bạn là Web Developer trong một team phát triển e-commerce.

Product Owner tạo task:

> **Add an order cancellation feature.**

Requirement ban đầu:

> Users should be able to cancel an order before it is shipped.

Bạn thấy requirement chưa đủ rõ.

## Task A — Clarify

Viết 5 câu hỏi:

- Khi nào user được cancel?
- Điều gì xảy ra nếu order đã shipped?
- Có hoàn tiền không?
- Có giới hạn thời gian không?
- API trả về status code nào?

Dùng:

```text
Could you clarify...?
What should happen if...?
Does the feature...?
Are there any...?
Could you provide...?
```

---

# 2. Daily Standup

Ngày hôm sau bạn báo cáo:

> Yesterday, I reviewed the cancellation requirements and started implementing the API.

> Today, I am working on the database changes and tests.

> I currently have no blockers.

Hãy tự viết phiên bản của bạn.

---

# 3. Bug Investigation

Trong quá trình test, bạn phát hiện:

> The cancellation API returns a 500 error when the order has already been shipped.

Viết:

```text
Expected behavior:
Actual behavior:
Steps to reproduce:
Possible cause:
Impact:
```

---

# 4. Technical Discussion

Team hỏi:

> Should we allow cancellation after the order has been shipped?

Bạn cần đưa ra ý kiến.

Dùng:

```text
I think we should...
One possible approach is...
The main advantage is...
The main drawback is...
I would recommend...
```

Viết 6–8 câu.

---

# 5. Pull Request

Sau khi fix xong, viết PR description:

```text
## Summary

## What changed

## Why

## Testing

## Notes
```

---

# 6. Code Review

Reviewer viết:

> Could you add a test for the case where the order has already been shipped?

Bạn trả lời:

> I've added the test and pushed the changes.

Sau đó reviewer hỏi:

> Why do we return a 409 instead of a 400?

Bạn trả lời bằng 3–5 câu English.

---

# 7. Final Standup

Cuối ngày:

> I finished the cancellation API and added the required tests. The pull request has been reviewed and approved. The feature is ready to be deployed to staging.

Hãy viết lại bằng cách của bạn.

---

# 8. Final Translation

Dịch đoạn sau:

> The cancellation feature allows users to cancel an order before it is shipped. The API validates the current order status before processing the cancellation request. If the order has already been shipped, the API returns an appropriate error response. The implementation also includes tests for successful cancellation, invalid requests, and orders that can no longer be cancelled.

---

# 9. Reverse Translation

Dịch sang English:

> Tính năng hủy đơn hàng cho phép người dùng hủy đơn trước khi đơn được giao cho đơn vị vận chuyển. API kiểm tra trạng thái hiện tại của đơn hàng trước khi xử lý request. Nếu đơn hàng đã được giao cho đơn vị vận chuyển, API trả về lỗi phù hợp. Implementation bao gồm test cho trường hợp hủy thành công, request không hợp lệ và đơn hàng không thể hủy.

---

# 10. Phase 2 Final Challenge

Không nhìn lại các bài trước, hãy hoàn thành toàn bộ workflow:

1. Clarify một requirement.
2. Viết daily standup.
3. Mô tả một bug.
4. Đề xuất solution.
5. Viết PR description.
6. Trả lời một code review comment.
7. Viết technical note ngắn.

Nếu bạn làm được 7 phần này bằng English mà không phải dịch từng câu trong đầu, bạn đã bắt đầu chuyển từ **IT English học thuật → Workplace English thực tế**.

---

# 11. 80/20 Master Patterns

```text
Could you clarify...?
What should happen if...?
I am currently working on...
I am blocked by...
I think we should...
One possible approach is...
The main advantage is...
The main drawback is...
Could you take a look...?
I've addressed your comments.
The issue occurs when...
The root cause is...
This document describes...
The endpoint is used to...
The request must contain...
Once this is done, I will...
```

## Phase 2 Goal

> **Understand → ask → explain → discuss → write → respond.**

Bạn không cần nói English hoàn hảo.

Mục tiêu là **truyền đạt đúng ý trong công việc Web Developer một cách rõ ràng và tự nhiên.**
