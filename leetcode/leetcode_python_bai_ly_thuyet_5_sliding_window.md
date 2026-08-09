# Bài lý thuyết 5/10 — Sliding Window

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Sliding Window là gì.
- Khi nào dùng Fixed Window.
- Khi nào dùng Dynamic Window.
- Vì sao Sliding Window thường giảm `O(n²)` xuống `O(n)`.
- Dấu hiệu nhận biết: contiguous, longest, shortest, substring, subarray.
- Cách quản lý `left`, `right` và trạng thái trong window.

---

## 1. Sliding Window là gì?

Sliding Window là kỹ thuật duy trì một đoạn liên tiếp trong Array hoặc String.

Ví dụ:

```text
nums = [1, 2, 3, 4, 5, 6]

          [2, 3, 4]
           ↑     ↑
         left  right
```

Window là đoạn:

```text
left ... right
```

Nó luôn là một đoạn **contiguous**.

---

## 2. Dấu hiệu quan trọng nhất

Khi đề có:

```text
contiguous subarray
```

hoặc:

```text
substring
```

hãy bắt đầu nghĩ tới:

```text
Sliding Window
```

Đặc biệt nếu đề hỏi:

```text
longest
shortest
maximum
minimum
```

trên một đoạn liên tiếp.

---

## 3. Fixed Window

Fixed Window có kích thước cố định.

Ví dụ:

> Tìm tổng lớn nhất của subarray có độ dài `k = 3`.

```text
[1, 2, 3, 4, 5]

[1, 2, 3]
   [2, 3, 4]
      [3, 4, 5]
```

Mỗi window có đúng 3 phần tử.

---

## 4. Brute Force của Fixed Window

Ta có thể cộng lại từng window.

Ví dụ:

```text
window 1 → 1 + 2 + 3
window 2 → 2 + 3 + 4
window 3 → 3 + 4 + 5
```

Nếu mỗi window dài `k`, ta có thể mất:

```text
O(n * k)
```

Nếu `k` gần `n`, có thể gần:

```text
O(n²)
```

---

## 5. Tối ưu Fixed Window

Ta không cần tính lại toàn bộ.

Ví dụ:

```text
[1, 2, 3] → sum = 6
```

Window tiếp theo:

```text
[2, 3, 4]
```

Ta chỉ cần:

```text
sum = sum - 1 + 4
```

Tức là:

```text
remove phần tử rời window
add phần tử mới vào window
```

Pattern:

```text
Old Window
- outgoing
+ incoming
→ New Window
```

Time Complexity:

```text
O(n)
```

---

## 6. Dynamic Window

Dynamic Window có kích thước thay đổi.

Ví dụ:

> Tìm substring dài nhất không có ký tự lặp.

Ta có:

```text
right → mở rộng window
left  → thu nhỏ khi vi phạm điều kiện
```

Hình dung:

```text
a b c a b c
↑     ↑
L     R
```

Nếu thêm character mới làm window invalid:

```text
move left
```

cho đến khi window hợp lệ trở lại.

---

## 7. Quy tắc Dynamic Window

Một pattern rất phổ biến:

```python
left = 0

for right in range(len(nums)):
    # add nums[right] vào window

    while window_invalid:
        # remove nums[left]
        left += 1

    # update answer
```

Điều quan trọng không phải học thuộc code.

Cần hiểu:

```text
right mở rộng
left sửa lỗi
```

---

## 8. Khi nào dùng `while`?

Trong Dynamic Window:

```python
while window_invalid:
```

vì có thể cần thu nhỏ nhiều lần.

Ví dụ:

```text
window đang có nhiều phần tử vi phạm
```

Ta phải move `left` cho tới khi hợp lệ.

---

## 9. Window state

Trong window, ta thường phải lưu thông tin như:

```text
current_sum
frequency
set of characters
number of distinct items
```

Ví dụ:

```text
Longest substring without repeating characters
→ Hash Set / Hash Map + Sliding Window
```

---

## 10. Sliding Window + Hash Set

Ví dụ String:

```text
abcabcbb
```

Ta cần biết:

> Character mới đã tồn tại trong window chưa?

Dùng:

```python
seen = set()
```

Khi character mới chưa tồn tại:

```text
expand right
```

Khi duplicate:

```text
remove từ left
```

Pattern:

```text
Longest substring + no duplicate
→ Sliding Window + Hash Set
```

---

## 11. Sliding Window + Hash Map

Nếu cần frequency:

```text
window có bao nhiêu lần xuất hiện của mỗi character?
```

Ta dùng:

```python
freq = {}
```

Pattern:

```text
Window condition dựa trên frequency
→ Sliding Window + Hash Map
```

---

## 12. Vì sao vẫn là `O(n)`?

Có thể thấy cả `left` và `right` đều di chuyển.

Nhưng:

```text
right chỉ đi từ trái → phải
left chỉ đi từ trái → phải
```

Mỗi pointer đi tối đa `n` bước.

Tổng vẫn:

```text
O(n)
```

Không phải `O(n²)` nếu chúng không reset lại nhiều lần.

---

## 13. Fixed vs Dynamic Window

### Fixed Window

Dấu hiệu:

```text
subarray of size k
exactly k
length k
```

### Dynamic Window

Dấu hiệu:

```text
longest
shortest
at most
at least
without repeating
condition changes
```

---

## 14. Khi Sliding Window không phù hợp?

Không phải mọi subarray đều dùng Sliding Window.

Ví dụ:

```text
Subarray Sum Equals K
```

Nếu có số âm, việc tăng/giảm window không còn đơn điệu.

Khi đó có thể cần:

```text
Prefix Sum + Hash Map
```

Do đó cần nhìn điều kiện kỹ.

---

## 15. Những lỗi thường gặp

### Lỗi 1

Update answer trước khi window hợp lệ.

### Lỗi 2

Quên remove state của `nums[left]` khi move left.

### Lỗi 3

Dùng `if` thay vì `while` khi cần thu nhỏ nhiều lần.

### Lỗi 4

Không xác định rõ window là:

```text
[left, right]
```

hay:

```text
[left, right)
```

---

## 16. Complexity

Fixed Window:

```text
Time: O(n)
Space: O(1)
```

nếu chỉ giữ sum.

Dynamic Window:

```text
Time: O(n)
Space: tùy state
```

Nếu dùng Hash Map/Set:

```text
Space có thể O(n)
```

---

## 17. Pattern cần ghi nhớ

```text
Contiguous subarray
→ Sliding Window / Prefix Sum
```

```text
Longest/Shortest substring
→ Sliding Window
```

```text
Fixed size k
→ Fixed Window
```

```text
Condition-based size
→ Dynamic Window
```

```text
No duplicate
→ Sliding Window + Hash Set
```

---

## 18. Kiểm tra nhanh

### Câu 1

“Maximum sum of subarray of size `k`” gợi ý:

- A. Fixed Window
- B. DFS
- C. Binary Search

### Câu 2

Dynamic Window thường dùng hai pointer nào?

- A. `left`, `right`
- B. `top`, `bottom`
- C. `low`, `mid`

### Câu 3

Khi window invalid, pointer nào thường move?

- A. `left`
- B. `right`

### Câu 4

Sliding Window thường có Time Complexity:

- A. `O(n)`
- B. `O(n²)`
- C. `O(log n)`

### Câu 5

“Longest substring without repeating characters” gợi ý:

- A. Sliding Window + Hash Set
- B. Prefix Sum
- C. DFS
