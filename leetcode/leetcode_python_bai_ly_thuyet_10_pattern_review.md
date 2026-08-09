# Bài lý thuyết 10/10 — Pattern Recognition & Complexity Review

## Mục tiêu

Bài cuối cùng không giới thiệu thêm cấu trúc dữ liệu mới.

Mục tiêu là kết nối toàn bộ nền tảng:

```text
Problem
→ Observation
→ Pattern
→ Brute Force
→ Bottleneck
→ Optimization
→ Code
→ Complexity
```

Sau bài này, bạn cần bắt đầu nhìn đề và tự đặt câu hỏi đúng trước khi code.

---

## 1. Pattern Recognition quan trọng hơn học thuộc code

Hai bài có thể khác nội dung nhưng cùng pattern.

Ví dụ:

```text
Find duplicate number
Contains Duplicate
Unique characters
```

có thể đều dẫn tới:

```text
Hash Set
```

Mục tiêu:

> Nhìn cấu trúc bài toán, không nhìn tên bài.

---

## 2. Array — One Pass

Dấu hiệu:

```text
max
min
count
sum
best value so far
```

Pattern:

```text
One Pass + State
```

Ví dụ:

```text
maximum
→ max_so_far
```

```text
count condition
→ counter
```

```text
sum
→ accumulator
```

---

## 3. Hash Set

Dấu hiệu:

```text
duplicate
seen before
unique
exists?
```

Pattern:

```text
Hash Set
```

Câu hỏi tự hỏi:

> Tôi chỉ cần biết phần tử này đã xuất hiện chưa?

Nếu đúng, nghĩ tới `set`.

---

## 4. Hash Map

Dấu hiệu:

```text
frequency
count per value
mapping
value → index
pair + target
```

Pattern:

```text
Hash Map
```

Câu hỏi:

> Tôi cần gắn thêm thông tin gì với mỗi value?

---

## 5. Two Pointers

Dấu hiệu:

```text
Sorted Array
pair
palindrome
both ends
in-place remove/move
```

Pattern:

```text
Two Pointers
```

Câu hỏi:

> Có thể dùng hai vị trí để tránh nested loop không?

---

## 6. Sliding Window

Dấu hiệu:

```text
contiguous
subarray
substring
longest
shortest
size k
```

Pattern:

```text
Sliding Window
```

Câu hỏi:

> Khi window di chuyển, tôi có thể update state thay vì tính lại từ đầu không?

---

## 7. Prefix Sum

Dấu hiệu:

```text
range sum
many sum queries
subarray sum
left sum / right sum
```

Pattern:

```text
Prefix Sum
```

Câu hỏi:

> Tôi có đang cộng lại cùng một đoạn nhiều lần không?

---

## 8. Binary Search

Dấu hiệu:

```text
sorted
search
first/last position
monotonic
```

Pattern:

```text
Binary Search
```

Câu hỏi:

> Tôi có thể loại bỏ một nửa search space sau mỗi bước không?

---

## 9. Matrix

Dấu hiệu:

```text
grid
row
column
neighbor
diagonal
```

Pattern:

```text
Matrix Traversal
```

Cần xác định:

```text
rows
cols
boundary
coordinate
```

---

## 10. DFS/BFS Matrix

Dấu hiệu:

```text
connected cells
island
region
flood fill
shortest path
spread by level
```

Pattern:

```text
DFS / BFS
```

---

## 11. Pattern Map tổng hợp

| Dấu hiệu | Pattern nên nghĩ tới |
|---|---|
| Maximum / Minimum | One Pass + State |
| Count theo điều kiện | Counter |
| Duplicate | Hash Set |
| Frequency | Hash Map |
| Pair + Target | Hash Map / Two Pointers |
| Sorted Array | Binary Search / Two Pointers |
| Palindrome | Two Pointers |
| Contiguous subarray | Sliding Window / Prefix Sum |
| Longest/Shortest substring | Sliding Window |
| Range Sum | Prefix Sum |
| Subarray Sum Equals K | Prefix Sum + Hash Map |
| Grid + connected cells | DFS/BFS |
| Shortest path in unweighted grid | BFS |

---

## 12. Brute Force trước khi tối ưu

Không nên bỏ qua Brute Force.

Quy trình:

```text
1. Cách đơn giản nhất là gì?
2. Time Complexity?
3. Bottleneck nằm ở đâu?
4. Có thao tác lặp lại không?
5. Có search nhiều lần không?
6. Có thể lưu kết quả trước không?
7. Có property sorted/contiguous không?
```

Brute Force giúp ta thấy lý do cần pattern tối ưu.

---

## 13. Bottleneck thường gặp

### Nested Loop

```text
O(n²)
```

Có thể tối ưu bằng:

```text
Hash Map
Two Pointers
Sliding Window
```

### Search lặp lại

```text
list membership O(n)
```

Có thể đổi thành:

```text
Hash Set / Hash Map O(1) average
```

### Sum lặp lại

Có thể dùng:

```text
Prefix Sum
```

### Search Space lớn

Nếu ordered/monotonic:

```text
Binary Search
```

---

## 14. Time Complexity cần thuộc bản chất

### `O(1)`

Ví dụ:

```python
nums[i]
```

### `O(log n)`

Ví dụ:

```text
Binary Search
```

### `O(n)`

Ví dụ:

```text
One Pass
Two Pointers
Sliding Window
```

### `O(n²)`

Ví dụ:

```text
Nested Loop
```

Với Matrix:

```text
O(rows * cols)
```

---

## 15. Space Complexity cần phân biệt

### `O(1)`

Chỉ vài biến:

```text
left
right
sum
count
```

### `O(n)`

Dùng:

```text
Hash Map
Hash Set
new Array
queue
visited
```

có thể tăng theo input.

---

## 16. Trade-off Time vs Space

Ví dụ Two Sum:

### Brute Force

```text
Time: O(n²)
Space: O(1)
```

### Hash Map

```text
Time: O(n)
Space: O(n)
```

Tối ưu không phải luôn giảm cả Time và Space.

Ta thường:

```text
dùng thêm memory
→ giảm thời gian
```

---

## 17. Quy trình chuẩn khi gặp bài mới

### Bước 1 — Hiểu đề

```text
Input?
Output?
```

### Bước 2 — Ví dụ nhỏ

Tự dry-run.

### Bước 3 — Tìm từ khóa

Ví dụ:

```text
sorted
pair
duplicate
contiguous
longest
grid
```

### Bước 4 — Brute Force

Nói được cách đơn giản nhất.

### Bước 5 — Complexity

Brute Force đang là:

```text
O(n)?
O(n²)?
```

### Bước 6 — Bottleneck

Tìm thao tác tốn nhất.

### Bước 7 — Chọn Pattern

Dựa vào observation.

### Bước 8 — Code

Sau khi hiểu logic.

### Bước 9 — Dry-run

Chạy tay một ví dụ.

### Bước 10 — Complexity cuối

```text
Time?
Space?
```

---

## 18. Checklist tự hỏi

Trước khi code:

```text
Input có sorted không?
Có duplicate không?
Có pair + target không?
Có contiguous subarray/substring không?
Có range sum không?
Có cần index không?
Có grid không?
Có connected cells không?
Có thể giảm search space một nửa không?
```

---

## 19. Không học thuộc template

Ví dụ:

```python
while left < right:
```

không có ý nghĩa nếu bạn không biết:

```text
left đại diện gì?
right đại diện gì?
condition nào làm pointer di chuyển?
```

Tương tự:

```python
freq = {}
```

không có ý nghĩa nếu không biết:

```text
key là gì?
value là gì?
tại sao phải lưu?
```

---

## 20. Foundation Roadmap đã hoàn thành về lý thuyết

Bạn đã có nền tảng lý thuyết cho:

```text
Python for LeetCode
↓
Array
↓
String / Character
↓
Hash Map / Hash Set
↓
Two Pointers
↓
Sliding Window
↓
Prefix Sum
↓
Binary Search
↓
Matrix
↓
DFS / BFS Matrix
↓
Pattern Recognition Review
```

Bước tiếp theo là thực hành theo độ khó:

```text
Easy
→ Easy+
→ Medium
→ Medium+
```

---

## 21. Mục tiêu trong giai đoạn thực hành

Không phải:

```text
nhớ 50 solution
```

Mà là:

```text
nhìn 50 bài
→ rút ra 8–10 pattern
```

Mỗi bài cần đi qua:

```text
Problem
→ Observation
→ Pattern
→ Brute Force
→ Bottleneck
→ Optimization
→ Code
→ Complexity
```

---

## 22. Bảng tự đánh giá

| Kỹ năng | Mục tiêu |
|---|---|
| Đọc Input/Output | Tự làm được |
| Dry-run | Tự làm được |
| Nhận diện Brute Force | Tự làm được |
| Tính `O(n)`, `O(n²)` | Chắc |
| Hash Map/Set | Chắc |
| Two Pointers | Nhận diện được |
| Sliding Window | Nhận diện cơ bản |
| Prefix Sum | Hiểu Range Sum |
| Binary Search | Hiểu search space |
| Matrix | Chắc boundary |
| DFS/BFS Matrix | Hiểu connected cells |

---

## 23. Kiểm tra tổng hợp

### Câu 1

```text
Pair + target
```

gợi ý pattern nào?

### Câu 2

```text
Longest substring
```

gợi ý pattern nào?

### Câu 3

```text
Range Sum
```

gợi ý pattern nào?

### Câu 4

```text
Sorted Array + Search
```

gợi ý pattern nào?

### Câu 5

```text
Grid + connected cells
```

gợi ý pattern nào?

### Câu 6

Nested loop trên Array thường có complexity gì?

### Câu 7

Hash Set membership trung bình là gì?

### Câu 8

Binary Search là gì về mặt tư duy?

### Câu 9

Khi nào Hash Map tốt hơn Hash Set?

### Câu 10

Mục tiêu cuối cùng của roadmap là gì?

---

## Kết luận

Pattern quan trọng nhất cần ghi nhớ:

```text
Duplicate
→ Hash Set
```

```text
Frequency
→ Hash Map
```

```text
Pair + Target
→ Hash Map / Two Pointers
```

```text
Sorted Array
→ Binary Search / Two Pointers
```

```text
Palindrome
→ Two Pointers
```

```text
Contiguous subarray
→ Sliding Window / Prefix Sum
```

```text
Longest/Shortest substring
→ Sliding Window
```

```text
Range Sum
→ Prefix Sum
```

```text
Grid + connected cells
→ DFS / BFS
```

Mục tiêu:

```text
Không học thuộc code.
Học cách suy luận ra code.
```
