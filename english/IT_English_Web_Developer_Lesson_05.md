# IT English for Web Developers — Lesson 5

## Software Architecture

**Thời lượng:** 120 phút  
**Mục tiêu:** Đọc hiểu các đoạn mô tả architecture, components, services, dependencies và scalability.

---

## 1. Core Vocabulary

| English | Vietnamese | Common phrases |
|---|---|---|
| architecture | kiến trúc | system architecture |
| component | thành phần | system component |
| service | dịch vụ | backend service |
| module | module | application module |
| dependency | sự phụ thuộc | external dependency |
| interface | giao diện | programming interface |
| monolith | hệ thống nguyên khối | monolithic application |
| microservice | microservice | microservice architecture |
| scalability | khả năng mở rộng | improve scalability |
| reliability | độ tin cậy | system reliability |
| availability | tính sẵn sàng | high availability |
| maintainability | khả năng bảo trì | improve maintainability |
| resilience | khả năng chống chịu | system resilience |
| load | tải | database load |
| cache | bộ nhớ đệm | use a cache |

---

# 2. Essential Collocations

```text
design an architecture
define a component
separate a service
manage dependencies
reduce dependency
improve scalability
improve reliability
increase availability
improve maintainability
handle high traffic
reduce database load
use a cache
scale horizontally
scale vertically
```

---

# 3. Sentence Patterns

> The application consists of several services.

> Each service is responsible for a specific function.

> The frontend communicates with the backend through an API.

> The backend depends on a database.

> We introduced a cache to reduce database load.

> This architecture allows the system to scale horizontally.

> The service handles requests from multiple clients.

> The component is responsible for processing payments.

> The system is designed to handle high traffic.

> We separated the service to improve maintainability.

---

# 4. Reading — A Simple Web Architecture

> A typical web application consists of several components. The frontend is responsible for presenting information to users, while the backend handles business logic and communicates with the database.
>
> The frontend sends requests to the backend through an API. The backend validates the requests, processes the business logic, and retrieves data from the database. It then returns a response to the frontend.
>
> As an application grows, the architecture may become more complex. Developers may separate parts of the system into independent services. This can improve maintainability and allow individual components to scale independently.
>
> Caching is another common technique. A cache can store frequently requested data and reduce the number of requests sent to the database. This can improve response time and reduce database load.

---

# 5. Reading Questions

1. What is the frontend responsible for?
2. What does the backend handle?
3. How does the frontend communicate with the backend?
4. Why might developers separate a system into independent services?
5. How can caching improve performance?

---

# 6. Translation — English → Vietnamese

1. The application consists of several components.
2. The frontend communicates with the backend through an API.
3. The backend is responsible for business logic.
4. The service retrieves data from the database.
5. We introduced a cache to reduce database load.
6. This architecture allows the system to scale horizontally.
7. Each service is responsible for a specific function.
8. The system is designed to handle high traffic.
9. The architecture improves maintainability.
10. The backend depends on several external services.

---

# 7. Vietnamese → English

1. Ứng dụng bao gồm nhiều component.
2. Frontend giao tiếp với backend thông qua API.
3. Backend chịu trách nhiệm xử lý business logic.
4. Service lấy dữ liệu từ database.
5. Chúng tôi sử dụng cache để giảm tải database.
6. Kiến trúc này cho phép hệ thống mở rộng theo chiều ngang.
7. Mỗi service chịu trách nhiệm cho một chức năng cụ thể.
8. Hệ thống được thiết kế để xử lý lượng truy cập lớn.
9. Kiến trúc này cải thiện khả năng bảo trì.
10. Backend phụ thuộc vào một số service bên ngoài.

---

# 8. Translation Challenge

> The system uses a layered architecture to separate different responsibilities. The presentation layer handles user interaction, while the application layer contains the main business logic. The data access layer communicates with the database. This separation makes the code easier to maintain and test because each layer has a clearly defined responsibility.

---

# 9. 80/20 Review

```text
system architecture
application component
backend service
business logic
external dependency
improve scalability
improve reliability
increase availability
improve maintainability
reduce database load
handle high traffic
scale horizontally
use a cache
```
