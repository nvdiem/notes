# Phase 2 — Lesson 4: Bug Reports & Issue Investigation

**Thời lượng:** 120 phút

## 1. Core Vocabulary

`bug`, `issue`, `reproduce`, `steps to reproduce`, `expected behavior`, `actual behavior`, `root cause`, `impact`, `severity`, `environment`, `workaround`, `fix`, `regression`.

## 2. Bug Report Template

```text
Title:
Environment:
Steps to reproduce:
Expected behavior:
Actual behavior:
Impact:
Possible cause:
```

## 3. Useful Patterns

> I was able to reproduce the issue.

> The issue occurs when...

> The expected behavior is...

> The actual behavior is...

> The issue only occurs in production.

> The problem seems to be related to...

> We suspect that the root cause is...

> The issue was caused by...

> As a temporary workaround, we can...

> The fix has been deployed to staging.

## 4. Reading — Production Bug

> Users reported that the checkout page sometimes returned a 500 error. The development team was able to reproduce the issue when a customer had more than one discount applied to an order.
>
> The expected behavior was for the system to calculate the final price correctly. Instead, the application threw an exception during the discount calculation.
>
> After checking the logs and stack trace, the team identified a null value in the discount calculation logic. The developer fixed the issue and added a regression test.
>
> The fix was deployed to staging first. After the QA team verified the fix, it was deployed to production.

## 5. Translation

1. We were able to reproduce the issue.
2. The issue occurs when the user has multiple discounts.
3. The expected behavior is to calculate the final price correctly.
4. The actual behavior is different.
5. The root cause was a null value.
6. We added a regression test.
7. The fix was deployed to staging.
8. The issue has been resolved.

## 6. Reverse Translation

1. Người dùng báo cáo rằng checkout đôi khi trả về lỗi 500.
2. Chúng tôi đã tái hiện được lỗi.
3. Vấn đề xảy ra khi đơn hàng có nhiều discount.
4. Nguyên nhân gốc là một giá trị null.
5. Chúng tôi đã thêm regression test.
6. Bản fix đã được deploy lên staging.

## 7. Practical Bug Report

Viết một bug report bằng English cho tình huống:

> API login trả về 500 khi password sai.

Dùng template ở trên.

**80/20:** `reproduce the issue` / `expected behavior` / `actual behavior` / `root cause` / `was caused by` / `deployed to staging`.
