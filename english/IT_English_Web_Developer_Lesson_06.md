# IT English for Web Developers — Lesson 6

## Debugging, Errors & Logs

**Thời lượng:** 120 phút  
**Mục tiêu:** Đọc hiểu bug reports, error messages, logs và mô tả quá trình debugging.

---

## 1. Core Vocabulary

| English | Vietnamese | Common phrases |
|---|---|---|
| error | lỗi | handle an error |
| exception | ngoại lệ | throw an exception |
| failure | sự thất bại | request failure |
| log | nhật ký hệ thống | application log |
| stack trace | dấu vết stack | read a stack trace |
| debug | gỡ lỗi | debug an application |
| reproduce | tái hiện | reproduce an issue |
| root cause | nguyên nhân gốc | find the root cause |
| unexpected | không mong đợi | unexpected behavior |
| invalid | không hợp lệ | invalid input |
| timeout | hết thời gian chờ | request timeout |
| retry | thử lại | retry a request |
| crash | bị sập | application crash |
| investigate | điều tra/xem xét | investigate an issue |
| configuration | cấu hình | configuration error |

---

# 2. Essential Collocations

```text
find a bug
report an issue
reproduce an issue
investigate an issue
debug an application
read the logs
check the stack trace
find the root cause
throw an exception
handle an error
fix the issue
retry the request
request timeout
configuration error
unexpected behavior
```

---

# 3. Sentence Patterns

> We were able to reproduce the issue.

> The application throws an exception when the input is invalid.

> The logs indicate that the database connection failed.

> The request timed out after 30 seconds.

> We need to identify the root cause.

> The issue was caused by an invalid configuration.

> The application crashes when the service is unavailable.

> We added a retry mechanism to handle temporary failures.

> The error occurs when the user submits an empty form.

> The stack trace shows where the exception occurred.

---

# 4. Reading — Investigating a Production Issue

> The development team received a report that users were unable to complete the login process. The team first tried to reproduce the issue in a test environment. However, the issue did not occur consistently.
>
> The developers then checked the application logs and found several timeout errors. The logs showed that the authentication service was sometimes unable to connect to the database.
>
> After investigating the problem, the team identified a configuration issue in the database connection settings. The team corrected the configuration and deployed the change to the staging environment.
>
> After additional testing, the login process worked as expected. The team then deployed the fix to production and continued monitoring the logs.

---

# 5. Reading Questions

1. What problem did users report?
2. Why was the issue difficult to reproduce?
3. What did the logs show?
4. What was the root cause?
5. Where did the team test the fix before production?

---

# 6. Translation — English → Vietnamese

1. We were able to reproduce the issue.
2. The application throws an exception when the input is invalid.
3. The logs indicate that the database connection failed.
4. The request timed out after 30 seconds.
5. We need to identify the root cause.
6. The issue was caused by an invalid configuration.
7. The application crashes when the service is unavailable.
8. We added a retry mechanism to handle temporary failures.
9. The error occurs when the user submits an empty form.
10. The stack trace shows where the exception occurred.

---

# 7. Vietnamese → English

1. Chúng tôi đã tái hiện được lỗi.
2. Log cho thấy kết nối database đã thất bại.
3. Request hết thời gian chờ sau 30 giây.
4. Chúng ta cần xác định nguyên nhân gốc.
5. Vấn đề được gây ra bởi cấu hình không hợp lệ.
6. Ứng dụng bị crash khi service không khả dụng.
7. Chúng tôi thêm cơ chế retry để xử lý lỗi tạm thời.
8. Lỗi xảy ra khi người dùng gửi form trống.
9. Stack trace cho biết exception xảy ra ở đâu.
10. Developer đang điều tra vấn đề.

---

# 8. Translation Challenge

> When the application started returning a large number of errors, the development team checked the logs to understand what was happening. The logs showed that requests to an external service were timing out. The team reproduced the issue and discovered that the service was responding more slowly than expected. They increased the timeout temporarily and added a retry mechanism while investigating a long-term solution.

---

# 9. 80/20 Review

```text
reproduce an issue
investigate an issue
check the logs
read a stack trace
find the root cause
throw an exception
handle an error
request timeout
retry a request
invalid input
unexpected behavior
configuration error
```
