# Phase 2 — Lesson 5: Technical Discussion & Proposing Solutions

**Thời lượng:** 120 phút

## 1. Core Vocabulary

`approach`, `solution`, `trade-off`, `performance`, `complexity`, `maintainability`, `scalability`, `alternative`, `benefit`, `drawback`, `recommend`, `consider`, `suggest`.

## 2. Essential Patterns

> I think we should...

> I suggest that we...

> One possible approach is to...

> Another option would be to...

> The main advantage is...

> The main drawback is...

> This approach may improve performance.

> However, it could increase complexity.

> We should consider...

> From a maintainability perspective...

> I would recommend...

## 3. Reading — Choosing an Approach

> We need to decide how to handle frequently requested data. One option is to query the database every time a client sends a request. This approach is simple, but it may increase database load.
>
> Another option is to introduce a cache. This could improve response time and reduce the number of database queries. However, caching also introduces additional complexity because the application needs to keep cached data up to date.
>
> From a performance perspective, I would recommend using a cache for data that does not change frequently. We should also define a clear cache expiration strategy.

## 4. Translation

1. I think we should use a cache.
2. One possible approach is to query the database directly.
3. Another option would be to use a background job.
4. The main advantage is better performance.
5. The main drawback is increased complexity.
6. We should consider the maintenance cost.
7. This approach may improve scalability.
8. I would recommend the second approach.

## 5. Reverse Translation

1. Tôi nghĩ chúng ta nên sử dụng cache.
2. Một cách tiếp cận có thể là query database trực tiếp.
3. Một lựa chọn khác là sử dụng background job.
4. Ưu điểm chính là hiệu năng tốt hơn.
5. Nhược điểm chính là độ phức tạp tăng lên.
6. Chúng ta nên cân nhắc chi phí bảo trì.
7. Tôi đề xuất phương án thứ hai.

## 6. Practical Discussion

Chọn một vấn đề:

> REST API vs GraphQL

hoặc:

> Monolith vs Microservices

Viết 8–10 câu English:

```text
My recommendation:
Reason:
Advantage:
Drawback:
Alternative:
Trade-off:
Conclusion:
```

**80/20:** `I think we should...` / `One option is...` / `Another option would be...` / `The main advantage...` / `The main drawback...` / `I would recommend...`
