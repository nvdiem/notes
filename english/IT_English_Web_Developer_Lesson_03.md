# IT English for Web Developers — Lesson 3

## Database & SQL

**Thời lượng:** 120 phút  
**Mục tiêu:** Đọc hiểu và dịch các đoạn văn về database, query, schema, index, migration và transaction.

---

## 1. Core Vocabulary

| English | Vietnamese | Common phrases |
|---|---|---|
| database | cơ sở dữ liệu | relational database |
| table | bảng | create a table |
| row | hàng/bản ghi | insert a row |
| column | cột | add a column |
| record | bản ghi | retrieve a record |
| query | truy vấn | run a query |
| schema | lược đồ CSDL | database schema |
| index | chỉ mục | create an index |
| constraint | ràng buộc | database constraint |
| relationship | mối quan hệ | define a relationship |
| primary key | khóa chính | primary key |
| foreign key | khóa ngoại | foreign key |
| transaction | giao dịch | start a transaction |
| migration | migration | run a migration |
| insert | chèn | insert data |
| retrieve | truy xuất | retrieve records |
| update | cập nhật | update a record |
| delete | xóa | delete a record |
| query performance | hiệu năng truy vấn | improve query performance |

---

# 2. Essential Collocations

```text
store data
retrieve data
query a database
run a query
insert a record
update a record
delete a record
create a table
add a column
create an index
define a relationship
enforce a constraint
run a migration
improve query performance
reduce database load
```

---

# 3. Sentence Patterns

### Pattern 1

> The application stores user data in a database.

### Pattern 2

> The query retrieves all active users.

### Pattern 3

> We need to add an index to improve query performance.

### Pattern 4

> The migration creates a new table.

### Pattern 5

> The table contains information about users.

### Pattern 6

> The foreign key references the users table.

### Pattern 7

> The transaction ensures that all operations are completed successfully.

### Pattern 8

> The application queries the database when a user opens the page.

### Pattern 9

> If the query fails, the application returns an error.

### Pattern 10

> This index helps reduce the time required to retrieve records.

---

# 4. Reading — How a Web Application Uses a Database

> Most web applications need a database to store and retrieve information. For example, an application may store users, products, orders, and payment records in a relational database.
>
> When a user requests information, the backend usually sends a query to the database. The database processes the query and returns the requested records. The backend then converts the result into a format that can be returned to the client.
>
> As the amount of data grows, query performance can become an issue. Developers may create indexes to make frequently used queries faster. However, indexes also require storage and can increase the cost of write operations.
>
> Database migrations are commonly used to change the database schema. A migration may create a new table, add a column, or modify an existing constraint. Before applying a migration in production, developers should test it carefully.

---

# 5. Reading Questions

1. Why do web applications need databases?
2. What happens when a user requests information?
3. Why are indexes used?
4. What is a possible disadvantage of indexes?
5. What can a database migration change?

---

# 6. Translation — English → Vietnamese

1. The application stores user data in a relational database.
2. The backend sends a query to the database.
3. The query retrieves all active users.
4. We need to add an index to improve query performance.
5. The migration creates a new table.
6. The foreign key references the users table.
7. The transaction ensures that all operations are completed successfully.
8. The database returns the requested records.
9. The application updates the record after the user submits the form.
10. Developers should test database migrations before deploying them to production.

---

# 7. Translation — Vietnamese → English

1. Ứng dụng lưu dữ liệu người dùng trong database.
2. Backend gửi một query đến database.
3. Query lấy tất cả người dùng đang hoạt động.
4. Chúng ta cần thêm index để cải thiện hiệu năng truy vấn.
5. Migration tạo một bảng mới.
6. Foreign key tham chiếu đến bảng users.
7. Database trả về các bản ghi được yêu cầu.
8. Ứng dụng cập nhật bản ghi sau khi người dùng gửi form.
9. Transaction đảm bảo rằng tất cả thao tác được hoàn thành thành công.
10. Developer nên kiểm thử migration trước khi triển khai lên production.

---

# 8. Translation Challenge

> The backend retrieves user information from the database whenever a client sends a request. The application first validates the request and then executes a database query. If the query returns the required records, the backend processes the result and sends a response to the client. To improve performance, the development team may add indexes to frequently queried columns.

---

# 9. Reverse Translation

> Khi người dùng yêu cầu thông tin, backend gửi một query đến database. Database xử lý query và trả về các bản ghi được yêu cầu. Backend sau đó xử lý kết quả và gửi response cho client. Khi lượng dữ liệu tăng lên, developer có thể cần thêm index để cải thiện hiệu năng truy vấn.

---

# 10. 80/20 Review

```text
store data
retrieve data
run a query
insert a record
update a record
delete a record
create an index
improve query performance
run a migration
database schema
primary key
foreign key
database transaction
```
