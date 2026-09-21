# IT English for Web Developers — Lesson 2

## Web, HTTP & REST API

**Thời lượng:** 120 phút  
**Mục tiêu:** Đọc hiểu và dịch các đoạn mô tả API, HTTP request/response và REST API.

---

## 1. Core Vocabulary

| English | Vietnamese | Common phrases |
|---|---|---|
| API | giao diện lập trình ứng dụng | design an API |
| endpoint | điểm cuối API | API endpoint |
| request | yêu cầu | send a request |
| response | phản hồi | receive a response |
| payload | dữ liệu gửi trong request | request payload |
| header | phần header | HTTP header |
| parameter | tham số | request parameter |
| resource | tài nguyên | retrieve a resource |
| client | phía client | API client |
| server | máy chủ | application server |
| status code | mã trạng thái | HTTP status code |
| authentication | xác thực | require authentication |
| authorization | phân quyền | check authorization |
| retrieve | lấy/truy xuất | retrieve data |
| submit | gửi | submit a request |
| validate | xác thực/kiểm tra hợp lệ | validate input |
| endpoint | endpoint | expose an endpoint |
| timeout | thời gian chờ hết hạn | request timeout |

---

# 2. Essential Collocations

```text
send a request
receive a response
make an API request
return a response
return a status code
validate a request
validate user input
retrieve data
send a payload
include a header
require authentication
check authorization
handle an error
expose an endpoint
call an API
```

---

# 3. Sentence Patterns

### Pattern 1 — The client sends...

> The client sends a request to the server.

### Pattern 2 — The API returns...

> The API returns a JSON response.

### Pattern 3 — The endpoint accepts...

> The endpoint accepts POST requests.

### Pattern 4 — require + noun

> The endpoint requires authentication.

### Pattern 5 — allow + object + to V

> The API allows clients to retrieve user data.

### Pattern 6 — when + clause

> The server returns a 404 status code when the resource cannot be found.

### Pattern 7 — be responsible for + V-ing

> The server is responsible for validating the request.

### Pattern 8 — be used to + V

> This endpoint is used to create a new user.

### Pattern 9 — if + clause

> If authentication fails, the server returns a 401 status code.

### Pattern 10 — in order to + V

> The client sends a token in order to authenticate the request.

---

# 4. HTTP Vocabulary You Should Recognize

```text
GET       retrieve data
POST      create/submit data
PUT       replace/update data
PATCH     partially update data
DELETE    remove data

200       successful request
201       resource created
400       bad request
401       authentication required/failed
403       forbidden
404       resource not found
500       internal server error
```

---

# 5. Reading — How a REST API Handles a Request

> A web application often communicates with a backend server through a REST API. When a client needs some data, it sends an HTTP request to a specific endpoint. The request may contain parameters, headers, and a payload.
>
> The server receives the request and validates the input. It may also check the user's authentication and authorization before processing the request. If everything is valid, the server performs the required operation and returns a response.
>
> The response usually contains a status code and a body. The body may contain JSON data that the client can use to update the user interface. If the server cannot process the request, it returns an appropriate error status code.
>
> For example, a client may send a GET request to retrieve a user's profile. If the user exists and the request is valid, the API returns a successful response. If the user cannot be found, the server returns a 404 status code.

---

# 6. Reading Questions

1. How does a client communicate with a backend server?
2. What can an HTTP request contain?
3. What does the server validate?
4. Why does the server check authentication and authorization?
5. What information can an HTTP response contain?

---

# 7. Translation — English → Vietnamese

1. The client sends a request to the API.
2. The endpoint requires authentication.
3. The server validates the request before processing it.
4. The API returns a JSON response.
5. The endpoint allows clients to retrieve user information.
6. The server returns a 404 status code when the resource cannot be found.
7. The request contains several parameters.
8. The client sends the authentication token in the request header.
9. The API handles invalid requests by returning an error response.
10. The server processes the request and returns the result.

---

# 8. Translation — Vietnamese → English

1. Client gửi một request đến server.
2. API trả về một JSON response.
3. Endpoint này yêu cầu authentication.
4. Server kiểm tra dữ liệu đầu vào trước khi xử lý request.
5. API cho phép client lấy thông tin người dùng.
6. Server trả về mã trạng thái 404 khi không tìm thấy tài nguyên.
7. Request chứa một số tham số.
8. Client gửi token trong request header.
9. Server xử lý request và trả về kết quả.
10. API trả về lỗi nếu request không hợp lệ.

---

# 9. Translation Challenge

> When a user opens a web page, the browser may need to retrieve data from the backend. It sends an HTTP request to an API endpoint, and the server processes the request. The server validates the request, checks authentication, and retrieves the required data from the database. It then returns a JSON response to the client. The client uses this response to display the data on the page.

---

# 10. Speaking Drill

Nói thành tiếng:

```text
The client sends a request.
The server processes the request.
The API validates the input.
The endpoint requires authentication.
The API returns a JSON response.
The client receives the response.
The server returns a status code.
The resource cannot be found.
The request contains a payload.
The API handles the error.
```

---

# 11. 80/20 Review

Ưu tiên nhớ:

```text
send a request
receive a response
API endpoint
request payload
request parameter
HTTP header
status code
validate input
retrieve data
require authentication
check authorization
handle an error
```

**Nguyên tắc:** học cả cụm, không học từ đơn lẻ.
