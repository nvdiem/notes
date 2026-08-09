# Bài lý thuyết 8/10 — Array 2D / Matrix

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Matrix được biểu diễn thế nào trong Python.
- Row, column, coordinate.
- Cách duyệt Matrix.
- Boundary check.
- Neighbor cells.
- Duyệt row, column, diagonal.
- Chuẩn bị nền tảng cho DFS/BFS trên Matrix.

---

## 1. Matrix là gì?

Ví dụ:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Ta có:

```text
1 2 3
4 5 6
7 8 9
```

Đây là Array 2 chiều.

---

## 2. Row và Column

```text
row = hàng
column = cột
```

Số hàng:

```python
rows = len(matrix)
```

Số cột:

```python
cols = len(matrix[0])
```

Với Matrix trên:

```text
rows = 3
cols = 3
```

---

## 3. Truy cập phần tử

Cú pháp:

```python
matrix[r][c]
```

Ví dụ:

```python
matrix[1][2]
```

→ `6`

Vì:

```text
row 1
column 2
```

---

## 4. Coordinate

Ta thường biểu diễn một cell bằng:

```text
(r, c)
```

Ví dụ:

```text
(0, 0)
```

là góc trên trái.

```text
(rows - 1, cols - 1)
```

là góc dưới phải.

---

## 5. Duyệt toàn Matrix

```python
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c])
```

Nếu Matrix có:

```text
rows × cols
```

cell, Time Complexity:

```text
O(rows * cols)
```

---

## 6. Duyệt từng row

```python
for row in matrix:
    for value in row:
        print(value)
```

Dùng khi không cần coordinate.

Nếu cần row/column index:

```python
for r in range(rows):
    for c in range(cols):
```

---

## 7. Duyệt một row cụ thể

Ví dụ row `1`:

```python
for c in range(cols):
    print(matrix[1][c])
```

---

## 8. Duyệt một column cụ thể

Ví dụ column `2`:

```python
for r in range(rows):
    print(matrix[r][2])
```

---

## 9. Main Diagonal

Với Matrix vuông:

```text
1 2 3
4 5 6
7 8 9
```

Main diagonal:

```text
1, 5, 9
```

Điều kiện:

```text
r == c
```

Code:

```python
for i in range(n):
    print(matrix[i][i])
```

---

## 10. Secondary Diagonal

Secondary diagonal:

```text
3, 5, 7
```

Điều kiện:

```text
r + c == n - 1
```

Hoặc:

```python
matrix[i][n - 1 - i]
```

---

## 11. Boundary

Một coordinate hợp lệ khi:

```text
0 <= r < rows
0 <= c < cols
```

Đây là điều kiện cực kỳ quan trọng.

Nếu sai boundary:

```python
matrix[r][c]
```

có thể gây `IndexError`.

---

## 12. Neighbor cells

Trong nhiều bài Matrix, mỗi cell có thể có 4 neighbor:

```text
up
down
left
right
```

Dùng:

```python
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
```

Với cell:

```text
(r, c)
```

neighbor:

```text
(r + dr, c + dc)
```

---

## 13. Boundary check cho neighbor

```python
nr = r + dr
nc = c + dc

if 0 <= nr < rows and 0 <= nc < cols:
    ...
```

Đây là mẫu code sẽ dùng rất nhiều trong DFS/BFS.

---

## 14. Duyệt Matrix theo layer

Một số bài như:

```text
Spiral Matrix
```

cần quản lý:

```text
top
bottom
left
right
```

Sau mỗi vòng, boundary co lại.

Đây là một dạng Two Pointers / boundary simulation trên Matrix.

---

## 15. Transpose Matrix

Transpose đổi:

```text
row ↔ column
```

Ví dụ:

```text
1 2 3
4 5 6
```

thành:

```text
1 4
2 5
3 6
```

Mapping:

```text
matrix[r][c]
→ result[c][r]
```

---

## 16. In-place hay tạo Matrix mới?

Một số bài cho phép:

```text
result = new matrix
```

Space:

```text
O(rows * cols)
```

Một số bài yêu cầu:

```text
modify matrix in-place
```

Khi đó cần cẩn thận hơn để không ghi đè dữ liệu chưa xử lý.

---

## 17. Complexity

Duyệt toàn Matrix:

```text
O(rows * cols)
```

Nếu Matrix vuông `n × n`:

```text
O(n²)
```

Space tùy bài.

Nếu chỉ dùng vài biến:

```text
O(1)
```

Nếu tạo Matrix mới:

```text
O(rows * cols)
```

---

## 18. Những lỗi thường gặp

### Lỗi 1

Nhầm:

```python
len(matrix)
```

với:

```python
len(matrix[0])
```

### Lỗi 2

Nhầm row với column.

### Lỗi 3

Quên boundary check.

### Lỗi 4

Dùng số row cho column trong Matrix không vuông.

---

## 19. Pattern cần ghi nhớ

```text
Matrix
→ rows + cols
```

```text
Need coordinate
→ (r, c)
```

```text
4-direction neighbors
→ directions
```

```text
Connected cells
→ DFS / BFS
```

```text
Matrix traversal
→ O(rows * cols)
```

---

## 20. Kiểm tra nhanh

### Câu 1

Số row:

```python
len(matrix)
```

Đúng hay sai?

### Câu 2

Số column thường là:

```python
len(matrix[0])
```

Đúng hay sai?

### Câu 3

Cell `(r, c)` hợp lệ khi điều kiện nào đúng?

### Câu 4

Duyệt Matrix `rows × cols` có Time Complexity:

- A. `O(rows + cols)`
- B. `O(rows * cols)`
- C. `O(log n)`

### Câu 5

Grid + connected cells thường gợi ý:

- A. DFS/BFS
- B. Prefix Sum
- C. Binary Search
