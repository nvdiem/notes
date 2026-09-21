# Phase 3 — Lesson 3: Database Migration Simulation

**Thời lượng:** 120–150 phút

## Scenario

Product yêu cầu thêm profile cho user.

Jira:

> Add user profile information.

Fields:

```text
display_name
avatar_url
bio
```

---

## 1. Clarify Requirements

Hỏi:

- fields nullable?
- maximum bio length?
- avatar URL validation?
- existing users?
- migration strategy?
- rollback?

Viết ít nhất 6 câu hỏi.

---

## 2. Technical Plan

Mô tả database change:

```text
users
    ↓
user_profiles
```

Viết 8 câu English.

Phải sử dụng:

```text
migration
schema
foreign key
constraint
nullable
rollback
```

---

## 3. Migration Risk

Bạn phát hiện production có 10 million users.

Viết một đoạn giải thích:

> Why should we be careful when running this migration?

Dùng:

```text
There is a risk that...
The migration may...
We should consider...
To reduce the risk...
```

---

## 4. Team Discussion

Đề xuất:

**Option A:** Add columns to `users`

**Option B:** Create `user_profiles`

Chọn một option và giải thích trade-off bằng English.

---

## 5. Testing

Viết test plan:

```text
Before migration:
During migration:
After migration:
Rollback:
```

---

## 6. Incident

Migration trên staging thất bại.

Error:

> Foreign key constraint violation.

Giải thích cho team:

- what happened
- possible cause
- next step

---

## 7. PR Description

Viết PR description cho migration.

---

## 8. Final Update

Báo cáo:

> Migration tested → issue fixed → rollback tested → ready for production.

---

## Success Criteria

Bạn có thể giải thích bằng English:

> How would you safely deploy a database migration to production?
