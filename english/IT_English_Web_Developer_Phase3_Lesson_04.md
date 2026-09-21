# Phase 3 — Lesson 4: Production Bug & Incident Simulation

**Thời lượng:** 150 phút

## Scenario

Alert:

> **Checkout API error rate increased to 8%.**

Users report:

> “I cannot complete my payment.”

---

## 1. First Response

Viết một message gửi team:

```text
We are currently investigating...
The impact appears to be...
I will update the team...
```

---

## 2. Investigation

Logs:

```text
PaymentServiceTimeout
Database connection timeout
Request duration: 30s
```

Viết:

```text
What we know:
What we don't know:
Next steps:
```

---

## 3. Reproduce

Mô tả:

> The issue occurs when the payment service takes longer than 30 seconds to respond.

Viết bug report đầy đủ.

---

## 4. Root Cause

Bạn phát hiện:

> Database connection pool is exhausted.

Giải thích root cause bằng 6–8 câu.

---

## 5. Immediate Mitigation

Đề xuất:

- restart service
- increase connection pool
- rollback recent deployment
- reduce traffic

Viết recommendation và trade-off.

---

## 6. Team Communication

Viết update:

> The root cause has been identified...

---

## 7. Fix

Mô tả permanent fix.

---

## 8. Post-Incident Summary

Viết:

```text
Incident:
Impact:
Root cause:
Resolution:
Prevention:
```

---

## Success Criteria

Bạn phải có thể giải thích incident từ đầu đến cuối bằng English rõ ràng.
