# Phase 3 — Lesson 7: Release & Deployment Simulation

**Thời lượng:** 150 phút

## Scenario

Bạn chuẩn bị release:

```text
Version: v2.4.0
Environment: Production
```

Feature:

> New payment flow.

---

## 1. Release Checklist

Viết checklist bằng English:

```text
Tests
Database migration
Environment variables
Deployment
Monitoring
Rollback
Documentation
```

---

## 2. Release Announcement

Viết message:

> We are preparing to deploy v2.4.0...

---

## 3. Deployment Problem

Sau deployment:

```text
Error rate: 0.5% → 7%
```

Bạn phải thông báo team.

---

## 4. Decision

Đưa ra lựa chọn:

```text
Continue monitoring
Rollback
Disable feature
Fix forward
```

Viết recommendation và lý do.

---

## 5. Rollback

Viết:

> We decided to roll back...

Giải thích:

- why
- impact
- next step

---

## 6. Post-Release

Sau rollback, viết:

```text
What happened:
Impact:
Action taken:
Next steps:
```

---

## Success Criteria

Bạn có thể điều phối bằng English một deployment đơn giản và giải thích quyết định khi có sự cố.
