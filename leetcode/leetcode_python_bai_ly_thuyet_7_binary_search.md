# Bài lý thuyết 7/10 — Binary Search

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Binary Search là gì.
- Tại sao cần Sorted Search Space.
- Cách dùng `left`, `right`, `mid`.
- Khi nào move `left`, khi nào move `right`.
- Time Complexity `O(log n)`.
- Binary Search on Answer ở mức nhận diện.

---

## 1. Binary Search là gì?

Binary Search là kỹ thuật loại bỏ một nửa search space sau mỗi bước.

Ví dụ:

```text
[1, 3, 5, 7, 9, 11, 13]
```

Tìm `11`.

Ta xem phần tử giữa:

```text
7
```

Vì:

```text
11 > 7
```

nên toàn bộ nửa trái có thể bỏ.

---

## 2. Điều kiện quan trọng

Binary Search cần search space có tính:

```text
ordered / monotonic
```

Trường hợp cơ bản nhất:

```text
Sorted Array
```

Dấu hiệu:

```text
Sorted Array + Search
→ Binary Search
```

---

## 3. Ba biến quan trọng

```python
left = 0
right = len(nums) - 1
```

Mid:

```python
mid = (left + right) // 2
```

Ta so sánh:

```python
nums[mid]
```

với:

```text
target
```

---

## 4. Ba trường hợp

### Trường hợp 1

```text
nums[mid] == target
```

→ tìm thấy.

### Trường hợp 2

```text
nums[mid] < target
```

Target phải nằm bên phải.

```python
left = mid + 1
```

### Trường hợp 3

```text
nums[mid] > target
```

Target phải nằm bên trái.

```python
right = mid - 1
```

---

## 5. Vì sao `mid + 1` và `mid - 1`?

Ta đã kiểm tra `mid`.

Nếu:

```text
nums[mid] < target
```

thì `mid` không thể là đáp án.

Do đó bỏ luôn:

```text
0 ... mid
```

Search space mới:

```text
mid + 1 ... right
```

---

## 6. Template cơ bản

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

Không nên chỉ học thuộc.

Phải hiểu mỗi update đang loại bỏ phần nào.

---

## 7. Dry-run

```python
nums = [1, 3, 5, 7, 9, 11]
target = 9
```

Ban đầu:

```text
left = 0
right = 5
mid = 2
nums[mid] = 5
```

Vì:

```text
5 < 9
```

→

```text
left = 3
```

Tiếp:

```text
left = 3
right = 5
mid = 4
nums[mid] = 9
```

Tìm thấy.

---

## 8. Time Complexity

Mỗi bước search space giảm một nửa:

```text
n
n/2
n/4
n/8
...
```

Số bước:

```text
log₂(n)
```

Do đó:

```text
O(log n)
```

---

## 9. So với Linear Search

Linear Search:

```text
O(n)
```

Binary Search:

```text
O(log n)
```

Ví dụ với khoảng 1,000,000 phần tử:

```text
Linear Search
→ có thể gần 1,000,000 bước
```

```text
Binary Search
→ khoảng 20 bước
```

---

## 10. `left <= right` hay `left < right`?

Binary Search có nhiều template.

Trong template tìm exact target:

```python
while left <= right:
```

là phổ biến.

Nhưng với bài tìm boundary hoặc Binary Search on Answer, có thể dùng:

```python
while left < right:
```

Quan trọng:

> Hãy hiểu invariant của search space, không học thuộc template một cách máy móc.

---

## 11. Search Insert Position

Nếu target không tồn tại, có thể cần trả về vị trí chèn.

Khi loop kết thúc:

```text
left
```

thường chính là vị trí insert.

Đây là một ứng dụng quan trọng của Binary Search.

---

## 12. First / Last Occurrence

Nếu có duplicate:

```text
[1, 2, 2, 2, 3]
```

và muốn:

```text
first 2
```

hoặc:

```text
last 2
```

ta vẫn Binary Search, nhưng khi tìm thấy chưa dừng ngay.

Ta tiếp tục search về một phía.

Đây là dạng boundary search.

---

## 13. Rotated Sorted Array

Ví dụ:

```text
[4, 5, 6, 7, 0, 1, 2]
```

Array vẫn có cấu trúc sorted từng phần.

Ta có thể dùng Binary Search nâng cao bằng cách xác định nửa nào đang sorted.

Đây là bài Medium sau khi nền tảng chắc.

---

## 14. Binary Search on Answer

Không phải lúc nào Binary Search cũng search trong Array.

Đôi khi search trong:

```text
possible answer range
```

Ví dụ dạng:

```text
minimum capacity
maximum feasible value
minimum speed
```

Nếu có tính đơn điệu:

```text
x nhỏ → fail
x lớn → pass
```

có thể Binary Search trên đáp án.

Hiện tại chỉ cần nhận diện, chưa cần học sâu.

---

## 15. Những lỗi thường gặp

### Lỗi 1

Quên sorted condition.

### Lỗi 2

Dùng:

```python
left = mid
```

trong template không phù hợp, gây infinite loop.

### Lỗi 3

Sai điều kiện:

```python
while left < right
```

vs:

```python
while left <= right
```

### Lỗi 4

Không xác định rõ search space.

---

## 16. Pattern cần ghi nhớ

```text
Sorted Array + Search
→ Binary Search
```

```text
Search space giảm một nửa
→ Binary Search
```

```text
First / Last position
→ Boundary Binary Search
```

```text
Monotonic answer
→ Binary Search on Answer
```

---

## 17. Kiểm tra nhanh

### Câu 1

Binary Search cơ bản yêu cầu:

- A. Sorted Array
- B. Hash Map
- C. Matrix

### Câu 2

Nếu:

```text
nums[mid] < target
```

thì:

- A. `left = mid + 1`
- B. `right = mid - 1`

### Câu 3

Binary Search có Time Complexity:

- A. `O(n)`
- B. `O(log n)`
- C. `O(n²)`

### Câu 4

Mỗi bước Binary Search loại bỏ khoảng bao nhiêu search space?

- A. Một phần tử
- B. Một nửa
- C. Toàn bộ

### Câu 5

Binary Search chỉ dùng để tìm một số trong Array. Đúng hay sai?
