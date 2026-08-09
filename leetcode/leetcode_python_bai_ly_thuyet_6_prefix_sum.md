# Bài lý thuyết 6/10 — Prefix Sum

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Prefix Sum là gì.
- Cách xây Prefix Sum.
- Cách tính Range Sum nhanh.
- Vì sao Prefix Sum tối ưu việc cộng lại nhiều lần.
- Pattern Subarray Sum.
- Prefix Sum kết hợp Hash Map.

---

## 1. Prefix Sum là gì?

Cho:

```python
nums = [2, 4, 1, 3]
```

Prefix Sum lưu tổng từ đầu tới từng vị trí.

```text
nums:    2   4   1   3
prefix:  2   6   7   10
```

Ý nghĩa:

```text
prefix[0] = 2
prefix[1] = 2 + 4 = 6
prefix[2] = 2 + 4 + 1 = 7
prefix[3] = 2 + 4 + 1 + 3 = 10
```

---

## 2. Cách xây Prefix Sum

```python
prefix = [0] * len(nums)

prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]
```

Pattern:

```text
prefix[i]
=
prefix[i - 1]
+
nums[i]
```

---

## 3. Biến thể có thêm số 0 đầu

Cách rất phổ biến:

```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)
```

Với:

```python
nums = [2, 4, 1, 3]
```

ta có:

```text
prefix = [0, 2, 6, 7, 10]
```

Cách này giúp công thức Range Sum đẹp hơn.

---

## 4. Range Sum

Giả sử cần tổng từ index `l` đến `r`.

Nếu Prefix Sum có `0` ở đầu:

```text
sum(l..r)
=
prefix[r + 1] - prefix[l]
```

Ví dụ:

```python
nums = [2, 4, 1, 3]
```

Tổng index `1` đến `3`:

```text
4 + 1 + 3 = 8
```

Dùng prefix:

```text
prefix[4] - prefix[1]
=
10 - 2
=
8
```

---

## 5. Tại sao Prefix Sum hữu ích?

Nếu chỉ hỏi một Range Sum:

```text
duyệt trực tiếp
→ O(n)
```

Nhưng nếu hỏi rất nhiều lần:

```text
Q queries
```

Brute Force có thể thành:

```text
O(Q * n)
```

Với Prefix Sum:

```text
build → O(n)
each query → O(1)
```

Tổng:

```text
O(n + Q)
```

---

## 6. Pattern Range Sum

Dấu hiệu:

```text
sum from l to r
range sum
many sum queries
```

→ nghĩ tới:

```text
Prefix Sum
```

---

## 7. Prefix Sum và Pivot Index

Ví dụ:

> Tìm index sao cho tổng bên trái bằng tổng bên phải.

Ta có thể giữ:

```text
left_sum
total_sum
```

Khi đứng tại `i`:

```text
right_sum
=
total_sum - left_sum - nums[i]
```

Đây cũng là tư duy Prefix Sum.

---

## 8. Subarray Sum

Subarray từ `i + 1` đến `j` có tổng:

```text
prefix[j] - prefix[i]
```

Nếu muốn tổng bằng `k`:

```text
prefix[j] - prefix[i] = k
```

Suy ra:

```text
prefix[i] = prefix[j] - k
```

Đây là observation rất quan trọng.

---

## 9. Prefix Sum + Hash Map

Trong bài:

```text
Subarray Sum Equals K
```

Ta duyệt và giữ:

```text
current_prefix_sum
```

Tại mỗi bước, hỏi:

```text
current_prefix_sum - k
```

đã từng xuất hiện chưa?

Nếu rồi, ta tìm được một subarray có tổng `k`.

Pattern:

```text
Subarray Sum Equals K
→ Prefix Sum + Hash Map
```

---

## 10. Tại sao Hash Map giúp?

Brute Force:

```text
thử mọi subarray
→ O(n²)
```

Prefix Sum + Hash Map:

```text
mỗi bước:
lookup prefix cần tìm
→ average O(1)
```

Duyệt một lần:

```text
O(n)
```

Space:

```text
O(n)
```

---

## 11. Prefix Sum không chỉ cho tổng

Ý tưởng Prefix còn có thể dùng cho:

```text
count
frequency
number of zeros
number of even numbers
```

Ví dụ:

```text
prefix_even[i]
=
số lượng số chẵn từ đầu đến i
```

Sau đó query một đoạn nhanh.

---

## 12. Prefix Sum 2D

Sau này với Matrix:

```text
sum rectangle
```

có thể dùng:

```text
2D Prefix Sum
```

Nhưng chưa cần học sâu ở giai đoạn này.

---

## 13. Những lỗi thường gặp

### Lỗi 1

Sai index do dùng prefix không có số `0` đầu.

### Lỗi 2

Nhầm:

```text
prefix[r] - prefix[l]
```

với:

```text
prefix[r + 1] - prefix[l]
```

### Lỗi 3

Quên lưu prefix sum `0` ban đầu.

Trong Prefix Sum + Hash Map, thường cần:

```python
freq = {0: 1}
```

để xử lý subarray bắt đầu từ index `0`.

---

## 14. Complexity

Build Prefix Sum:

```text
O(n)
```

Range query:

```text
O(1)
```

Space:

```text
O(n)
```

Nếu chỉ giữ `current_sum`:

```text
O(1)
```

---

## 15. Pattern cần ghi nhớ

```text
Range Sum
→ Prefix Sum
```

```text
Many range queries
→ Prefix Sum
```

```text
Subarray Sum Equals K
→ Prefix Sum + Hash Map
```

```text
left sum / right sum
→ Prefix Sum mindset
```

---

## 16. Kiểm tra nhanh

### Câu 1

Prefix Sum giúp Range Sum query từ `O(n)` xuống:

- A. `O(1)`
- B. `O(log n)`
- C. `O(n²)`

### Câu 2

Nếu dùng prefix có số 0 đầu:

```text
sum(l..r) = ?
```

### Câu 3

“Subarray Sum Equals K” thường gợi ý:

- A. Prefix Sum + Hash Map
- B. DFS
- C. Two Pointers

### Câu 4

Xây Prefix Sum cho `n` phần tử mất:

- A. `O(1)`
- B. `O(n)`
- C. `O(n²)`

### Câu 5

Prefix Sum chủ yếu hữu ích khi phải tính tổng đoạn nhiều lần. Đúng hay sai?
