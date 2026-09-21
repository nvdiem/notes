# Phase 3 — Lesson 5: API Performance Simulation

**Thời lượng:** 120–150 phút

## Scenario

Một API:

```text
GET /api/products
```

có response time trung bình:

```text
2.8 seconds
```

Target:

```text
< 500 ms
```

---

## 1. Problem Description

Viết bằng English:

- current performance
- target
- impact

---

## 2. Investigation

Bạn phát hiện:

```text
Slow database query
Missing index
Large response payload
Repeated queries
```

Giải thích từng vấn đề.

---

## 3. Proposal

Đề xuất:

```text
add index
optimize query
pagination
response compression
cache
```

Viết 10 câu English.

---

## 4. Technical Discussion

Team hỏi:

> Should we add caching immediately?

Trả lời có:

- recommendation
- reason
- risk
- alternative

---

## 5. Testing

Viết test plan:

```text
Before optimization
After optimization
Load test
Regression test
```

---

## 6. Final Report

Viết:

> Before: 2.8s  
> After: 420ms

Giải thích kết quả bằng English.

---

## Success Criteria

Bạn có thể trình bày:

> What caused the slow API and how did you improve it?

trong 1–2 phút.
