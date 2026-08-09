# Bài lý thuyết 9/10 — DFS/BFS trên Matrix

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Connected cells là gì.
- DFS và BFS trên Matrix.
- `visited`.
- 4-direction movement.
- Boundary check.
- Khi nào dùng recursion, khi nào dùng `deque`.
- Time/Space Complexity của traversal trên Grid.

---

## 1. Connected cells

Ví dụ:

```text
1 1 0
0 1 0
1 0 1
```

Nếu chỉ đi:

```text
up
down
left
right
```

thì nhóm:

```text
1 1
  1
```

là một connected component.

Các số `1` khác có thể thuộc component khác.

---

## 2. Dấu hiệu nhận biết

Khi đề có:

```text
Grid
+
connected cells
```

hãy nghĩ:

```text
DFS / BFS
```

Ví dụ:

- Number of Islands
- Flood Fill
- Max Area of Island
- Rotting Oranges

---

## 3. DFS là gì?

DFS = Depth-First Search.

Ý tưởng:

> Đi sâu theo một hướng cho đến khi không đi tiếp được, rồi quay lại.

Trên Matrix:

```text
start cell
↓
neighbor
↓
neighbor của neighbor
↓
...
```

---

## 4. DFS bằng recursion

Ví dụ skeleton:

```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return

    if matrix[r][c] != 1:
        return

    matrix[r][c] = 0

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

Điều quan trọng:

```text
boundary
base case
mark visited
explore neighbors
```

---

## 5. Vì sao phải mark visited?

Nếu không:

```text
A → B → A → B → ...
```

ta có thể lặp vô hạn.

Có hai cách phổ biến:

### Cách 1

Dùng:

```python
visited = set()
```

### Cách 2

Sửa trực tiếp Matrix:

```python
matrix[r][c] = 0
```

nếu đề cho phép.

---

## 6. BFS là gì?

BFS = Breadth-First Search.

Ý tưởng:

> Duyệt theo từng lớp gần → xa.

Dùng queue.

Trong Python:

```python
from collections import deque
```

Tạo queue:

```python
queue = deque()
```

Thêm:

```python
queue.append((r, c))
```

Lấy:

```python
r, c = queue.popleft()
```

---

## 7. BFS skeleton

```python
from collections import deque

queue = deque([(start_r, start_c)])

while queue:
    r, c = queue.popleft()

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if valid:
            queue.append((nr, nc))
```

---

## 8. 4 directions

```python
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
```

Ý nghĩa:

```text
down
up
right
left
```

---

## 9. Boundary check

```python
if 0 <= nr < rows and 0 <= nc < cols:
```

Đây là check bắt buộc trước khi truy cập:

```python
matrix[nr][nc]
```

---

## 10. DFS vs BFS

Cả hai đều có thể dùng để:

```text
traverse connected component
```

### DFS

Phù hợp khi:

```text
explore component
count area
mark visited
```

### BFS

Phù hợp khi:

```text
shortest path in unweighted grid
level-by-level process
spreading over time
```

Ví dụ:

```text
Rotting Oranges
```

rất tự nhiên với BFS.

---

## 11. Number of Islands

Observation:

```text
Mỗi lần gặp một cell đất chưa visited
→ đó là một island mới
```

Ta:

```text
count += 1
```

rồi DFS/BFS để mark toàn bộ island đó.

Pattern:

```text
Scan grid
+
gặp component mới
→ DFS/BFS
```

---

## 12. Max Area of Island

Thay vì chỉ mark visited, DFS có thể trả về:

```text
area
```

Ví dụ:

```text
area =
1
+
area of neighbors
```

Sau đó giữ:

```text
max_area
```

Pattern kết hợp:

```text
DFS
+
One Pass Best State
```

---

## 13. Multi-source BFS

Một số bài có nhiều điểm bắt đầu cùng lúc.

Ví dụ:

```text
Rotting Oranges
```

Ta đưa tất cả rotten oranges ban đầu vào queue.

Đây gọi là:

```text
Multi-source BFS
```

Sau đó BFS theo từng minute / level.

---

## 14. BFS theo level

Pattern:

```python
while queue:
    for _ in range(len(queue)):
        ...
```

Mỗi vòng ngoài tương ứng một level.

Dùng khi đề hỏi:

```text
minimum steps
minutes
distance
```

---

## 15. Time Complexity

Grid có:

```text
rows * cols
```

cells.

Nếu mỗi cell được visit tối đa một lần:

```text
O(rows * cols)
```

Cả DFS và BFS thường như vậy.

---

## 16. Space Complexity

DFS recursion stack worst case:

```text
O(rows * cols)
```

BFS queue worst case:

```text
O(rows * cols)
```

Visited set cũng có thể:

```text
O(rows * cols)
```

---

## 17. Những lỗi thường gặp

### Lỗi 1

Mark visited sau khi add vào queue quá muộn.

Có thể add cùng cell nhiều lần.

Thường nên mark ngay khi enqueue.

### Lỗi 2

Quên boundary.

### Lỗi 3

Không phân biệt row/column.

### Lỗi 4

DFS recursion quá sâu với Grid rất lớn.

Trong Python, BFS hoặc iterative DFS có thể an toàn hơn.

---

## 18. Pattern cần ghi nhớ

```text
Grid + connected cells
→ DFS / BFS
```

```text
Count components
→ scan + DFS/BFS
```

```text
Shortest path in unweighted grid
→ BFS
```

```text
Spread by minutes / levels
→ BFS
```

```text
Explore one component deeply
→ DFS
```

---

## 19. Kiểm tra nhanh

### Câu 1

Connected cells trong Grid thường gợi ý:

- A. DFS/BFS
- B. Binary Search
- C. Prefix Sum

### Câu 2

BFS dùng cấu trúc dữ liệu nào?

- A. Queue
- B. Stack only
- C. Hash Map only

### Câu 3

Trong Python, queue hiệu quả nên dùng:

- A. `deque`
- B. `list.pop(0)` ưu tiên
- C. tuple

### Câu 4

Nếu mỗi cell visit một lần, Time Complexity là:

- A. `O(rows * cols)`
- B. `O(rows + cols)`
- C. `O(log n)`

### Câu 5

Shortest path trong unweighted grid thường ưu tiên:

- A. BFS
- B. Prefix Sum
- C. Two Pointers
