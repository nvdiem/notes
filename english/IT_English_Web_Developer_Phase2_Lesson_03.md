# Phase 2 — Lesson 3: Code Review & Pull Requests

**Thời lượng:** 120 phút

## 1. Core Vocabulary

`pull request`, `review`, `feedback`, `comment`, `concern`, `suggestion`, `readability`, `maintainability`, `refactor`, `simplify`, `duplicate`, `logic`, `edge case`, `approval`.

## 2. Collocations

```text
review a pull request
leave a comment
address feedback
raise a concern
make a suggestion
request changes
approve a pull request
refactor the code
simplify the logic
improve readability
avoid duplication
handle an edge case
```

## 3. Useful Patterns

> Could you take a look at this function?

> I have a concern about this implementation.

> I suggest simplifying this logic.

> Could we extract this into a separate function?

> This code may be difficult to maintain.

> I think we can avoid duplicating this logic.

> Could you add a test for this edge case?

> I've addressed your comments.

> I made the requested changes.

> The pull request is ready for another review.

## 4. Reading — PR Review

> I reviewed the pull request and found a few things that we should address before merging it. First, the authentication logic is duplicated in two different functions. I suggest extracting it into a reusable function.
>
> I also noticed that the error handling is not consistent. Some errors return a detailed message, while others return a generic response. It would be better to use a consistent format.
>
> Finally, could you add a test for the case where the authentication token is expired? Once these changes are addressed, I think the pull request will be ready to merge.

## 5. Translation

1. Could you take a look at this function?
2. I have a concern about this implementation.
3. I suggest extracting this logic into a separate function.
4. The code contains duplicated logic.
5. Could you add a test for this edge case?
6. I've addressed your comments.
7. The pull request is ready for another review.
8. We should use a consistent error format.

## 6. Reverse Translation

1. Tôi có một vấn đề cần trao đổi về implementation này.
2. Tôi đề xuất tách logic này thành một function riêng.
3. Code đang bị lặp logic.
4. Bạn có thể thêm test cho edge case này không?
5. Tôi đã xử lý các comment của bạn.
6. Pull request đã sẵn sàng để review lại.

## 7. Practical PR Comment

Viết 5 comment English cho một PR:

- một comment hỏi clarification
- một suggestion
- một concern
- một request thêm test
- một comment báo đã xử lý feedback

**80/20:** `take a look` / `raise a concern` / `I suggest...` / `Could you...?` / `I've addressed...`
