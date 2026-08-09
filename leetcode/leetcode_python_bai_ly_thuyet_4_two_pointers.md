# Bài lý thuyết 4/10 — Two Pointers

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Two Pointers là gì.
- Hai dạng phổ biến: hai đầu và cùng chiều.
- Khi nào Sorted Array gợi ý Two Pointers.
- Tại sao Two Pointers có thể giảm `O(n²)` xuống `O(n)`.
- Pattern Palindrome, Pair in Sorted Array, In-place modification.
- Cách di chuyển `left` và `right`.

---

## 1. Two Pointers là gì?

Two Pointers là kỹ thuật dùng hai vị trí để duyệt dữ liệu.

Ví dụ:

```text
nums = [1, 2, 3, 4, 5]

        ↑           ↑
      left        right
```

Hai pointer có thể:

- đi từ hai đầu vào giữa
- cùng đi từ trái sang phải
- một nhanh, một chậm

Trong roadmap hiện tại, ta tập trung trước vào hai dạng đầu.

---

## 2. Dạng 1 — Hai đầu tiến vào giữa

Ví dụ:

```text
[1, 2, 3, 4, 5]
 ↑           ↑
left       right
```

Sau mỗi bước:

```text
left += 1
right -= 1
```

Dùng nhiều trong:

- Palindrome
- Sorted Array + Pair
- Reverse Array/String

---

## 3. Palindrome

Ví dụ:

```text
racecar
```

So sánh:

```text
r == r
a == a
c == c
```

Hình dung:

```text
r a c e c a r
↑           ↑
L           R
```

Nếu giống nhau:

```python
left += 1
right -= 1
```

Nếu khác:

```text
không phải Palindrome
```

Pattern:

```text
Palindrome
→ Two Pointers
```

---

## 4. Tại sao không cần so sánh mọi cặp?

Palindrome chỉ cần so sánh các cặp đối xứng:

```text
0 với n-1
1 với n-2
2 với n-3
...
```

Số bước khoảng `n/2`.

Big-O:

```text
O(n)
```

Không cần nested loop.

---

## 5. Sorted Array + Pair

Cho:

```python
nums = [1, 2, 4, 6, 10]
target = 8
```

Ta đặt:

```text
L = 1
R = 10
```

Tổng:

```text
1 + 10 = 11
```

Quá lớn.

Vì Array đã sorted, muốn tổng nhỏ hơn ta phải:

```text
right -= 1
```

Sau đó:

```text
1 + 6 = 7
```

Quá nhỏ.

Muốn tổng lớn hơn:

```text
left += 1
```

Sau đó:

```text
2 + 6 = 8
```

Tìm thấy.

---

## 6. Observation quan trọng

Với Sorted Array:

```text
sum < target
→ cần số lớn hơn
→ move left
```

```text
sum > target
→ cần số nhỏ hơn
→ move right
```

Đây chính là lý do Two Pointers hoạt động.

Nếu Array chưa sorted, logic này thường không còn đúng.

---

## 7. Brute Force vs Two Pointers

Brute Force tìm pair:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
```

→ `O(n²)`

Two Pointers trên Sorted Array:

```text
left chỉ đi sang phải
right chỉ đi sang trái
```

Mỗi pointer đi tối đa `n` bước.

→ `O(n)`

Pattern:

```text
Sorted Array + Pair
→ Two Pointers
```

---

## 8. Dạng 2 — Slow / Fast Pointer

Ví dụ:

```text
nums = [0, 1, 0, 3, 12]
```

Một pointer đọc dữ liệu:

```text
fast
```

Một pointer chỉ vị trí ghi:

```text
slow
```

Hình dung:

```text
slow → nơi cần đặt phần tử hợp lệ tiếp theo
fast → duyệt để tìm phần tử hợp lệ
```

Dạng này hay gặp trong:

- Move Zeroes
- Remove Duplicates
- Remove Element
- in-place array modification

---

## 9. Ví dụ tư duy Slow/Fast

Giả sử muốn đưa số khác `0` về trước.

```text
[0, 1, 0, 3, 12]
```

`fast` duyệt:

```text
0 → bỏ qua
1 → đưa về vị trí slow
0 → bỏ qua
3 → đưa về vị trí slow
12 → đưa về vị trí slow
```

Sau đó xử lý phần còn lại.

Điều quan trọng:

> Một pointer đọc, một pointer quản lý vị trí hợp lệ.

---

## 10. Khi nào nghĩ đến Two Pointers?

### Dấu hiệu 1

```text
Sorted Array
+
Pair / Sum
```

→ Two Pointers

### Dấu hiệu 2

```text
Palindrome
```

→ Two Pointers từ hai đầu

### Dấu hiệu 3

```text
Remove / Move / Compress in-place
```

→ Slow/Fast Pointers

### Dấu hiệu 4

```text
Need compare both ends
```

→ Two Pointers

---

## 11. `left < right` hay `left <= right`?

Với pair:

```python
while left < right:
```

Vì ta cần hai phần tử khác nhau.

Với một số Binary Search:

```python
while left <= right:
```

có thể phù hợp.

Đừng học thuộc điều kiện. Hãy hỏi:

> Khi `left == right`, còn cần xử lý một phần tử đó không?

Trong bài pair, thường không.

---

## 12. Two Pointers không phải lúc nào cũng cần Sorted Array

Palindrome không cần sorted.

Ví dụ:

```text
racecar
```

Ta vẫn dùng Two Pointers vì cấu trúc bài toán có tính đối xứng.

Do đó:

```text
Sorted Array
```

là một dấu hiệu mạnh, nhưng không phải điều kiện bắt buộc cho mọi Two Pointers problem.

---

## 13. Two Pointers vs Hash Map

Ví dụ Pair + Target.

Nếu Array **không sorted**:

```text
Hash Map thường rất phù hợp
```

Nếu Array **đã sorted**:

```text
Two Pointers thường rất đẹp
```

So sánh:

```text
Hash Map
Time: O(n)
Space: O(n)
```

```text
Two Pointers
Time: O(n)
Space: O(1)
```

Đây là trade-off quan trọng.

---

## 14. Two Pointers và in-place

Các bài như:

- Move Zeroes
- Remove Duplicates from Sorted Array
- Remove Element

thường yêu cầu:

```text
Không tạo Array mới
```

Dấu hiệu:

```text
modify nums in-place
```

→ hãy nghĩ tới Slow/Fast Pointers.

---

## 15. Một lỗi thường gặp: move sai pointer

Trong Pair + Target:

```text
sum < target
```

nếu bạn giảm `right`, tổng sẽ càng nhỏ hơn hoặc không giúp tăng lên.

Hướng đúng:

```text
sum < target
→ left += 1
```

Vì Array sorted tăng dần.

---

## 16. Một lỗi thường gặp: move cả hai pointer không có lý do

Không phải lúc nào cũng:

```python
left += 1
right -= 1
```

Ví dụ Pair + Target:

- tổng nhỏ → chỉ move `left`
- tổng lớn → chỉ move `right`
- tìm thấy → return

Pointer phải di chuyển dựa trên **observation**.

---

## 17. Complexity

Hai pointer nhìn như có hai biến, nhưng không có nghĩa là `O(n²)`.

Ví dụ:

```text
left đi tối đa n bước
right đi tối đa n bước
```

Tổng vẫn cùng bậc:

```text
O(n)
```

Không có nested traversal độc lập.

Extra Space thường:

```text
O(1)
```

---

## 18. Quy trình suy nghĩ

Khi gặp bài có dấu hiệu Two Pointers, hỏi:

```text
1. Dữ liệu có sorted không?
2. Có đang tìm pair không?
3. Có tính đối xứng không?
4. Có cần xử lý in-place không?
5. Mỗi pointer đại diện cho điều gì?
6. Điều kiện nào khiến pointer nào di chuyển?
7. Có đảm bảo mỗi pointer chỉ đi một chiều không?
```

---

## 19. Pattern cần ghi nhớ

```text
Palindrome
→ left/right từ hai đầu
```

```text
Sorted Array + Pair
→ Two Pointers
```

```text
sum < target
→ move left
```

```text
sum > target
→ move right
```

```text
Remove / Move / Compress in-place
→ Slow/Fast
```

---

## 20. Kiểm tra nhanh

### Câu 1

Cho Sorted Array và cần tìm hai số có tổng bằng target. Pattern nên nghĩ tới là gì?

- A. Two Pointers
- B. DFS
- C. Prefix Sum

### Câu 2

Trong Array tăng dần, nếu:

```text
nums[left] + nums[right] < target
```

nên:

- A. `left += 1`
- B. `right -= 1`

### Câu 3

Palindrome thường đặt pointer ở đâu?

- A. Cả hai ở đầu
- B. Một đầu trái, một đầu phải
- C. Cả hai ở giữa

### Câu 4

Two Pointers trên Sorted Array thường có Time Complexity:

- A. `O(n)`
- B. `O(n²)`
- C. `O(log n)`

### Câu 5

Nếu bài yêu cầu sửa Array in-place, dạng Two Pointers nào thường hữu ích?

- A. Slow/Fast
- B. Binary Search
- C. Prefix Sum

---

## Pattern tổng kết

```text
Sorted Array
→ Two Pointers / Binary Search
```

```text
Sorted Array + Pair
→ Two Pointers
```

```text
Palindrome
→ Two Pointers
```

```text
In-place filter / move
→ Slow/Fast Pointers
```
