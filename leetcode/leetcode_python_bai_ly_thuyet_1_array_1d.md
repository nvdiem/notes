# Bài lý thuyết 1/10 — Array 1D

## Mục tiêu bài học

Sau bài này, bạn cần hiểu được:

- Array 1 chiều là gì.
- Cách truy cập phần tử bằng `index`.
- Cách duyệt Array.
- Khi nào cần `value`, khi nào cần `index`.
- Cách tìm `min`, `max`, `sum`, `count`.
- Cách giữ trạng thái khi duyệt.
- Cách nhận ra Brute Force bằng nested loop.
- Phân biệt `O(1)`, `O(n)`, `O(n²)` trong Array.
- Nhận diện những dạng bài Array cơ bản.

---

## 1. Array 1D là gì?

Trong Python, Array trên LeetCode thường được biểu diễn bằng `list`.

```python
nums = [4, 7, 2, 9, 5]
```

Ta có thể hình dung:

```text
Value:   4   7   2   9   5
Index:   0   1   2   3   4
```

Mỗi phần tử có:

```text
index → vị trí
value → giá trị
```

Ví dụ:

```python
nums[2]
```

kết quả:

```text
2
```

Vì:

```text
index 2 → value 2
```

---

## 2. Index là nền tảng của Array

Cho:

```python
nums = [10, 20, 30, 40]
```

Ta có:

```python
nums[0]  # 10
nums[1]  # 20
nums[2]  # 30
nums[3]  # 40
```

Nếu:

```python
n = len(nums)
```

thì index hợp lệ luôn là:

```text
0 → n - 1
```

Ví dụ:

```python
len(nums)
```

bằng `4`.

Nhưng:

```python
nums[4]
```

sẽ lỗi.

Vì phần tử cuối là:

```python
nums[3]
```

Đây gọi là lỗi **off-by-one** và xuất hiện rất nhiều khi mới học thuật toán.

---

## 3. Đọc phần tử trước và sau

Đây là kỹ năng rất hay dùng trong Array.

Cho:

```python
nums = [10, 20, 30, 40]
```

Nếu đang đứng ở:

```text
i = 2
```

thì:

```python
nums[i]
```

là:

```text
30
```

Phần tử trước:

```python
nums[i - 1]
```

→ `20`

Phần tử sau:

```python
nums[i + 1]
```

→ `40`

Hình dung:

```text
        i-1   i   i+1
         ↓    ↓    ↓
nums = [10,  20,  30,  40]
```

Tuy nhiên phải cẩn thận ở **boundary**.

Nếu:

```text
i = 0
```

thì không có phần tử bên trái theo logic của bài toán.

Nếu:

```text
i = n - 1
```

thì không có phần tử bên phải.

---

## 4. Duyệt Array theo value

Nếu chỉ cần từng giá trị:

```python
nums = [4, 7, 2]

for num in nums:
    print(num)
```

Quá trình:

```text
num = 4
num = 7
num = 2
```

Dùng kiểu này khi:

> Tôi chỉ quan tâm value.

Ví dụ tính tổng:

```python
total = 0

for num in nums:
    total += num
```

---

## 5. Duyệt Array theo index

Nếu cần vị trí:

```python
for i in range(len(nums)):
    print(i, nums[i])
```

Ví dụ:

```text
i = 0 → nums[0] = 4
i = 1 → nums[1] = 7
i = 2 → nums[2] = 2
```

Dùng khi:

- cần phần tử trước/sau
- cần trả về index
- cần thay đổi `nums[i]`
- cần so sánh các vị trí

Ví dụ:

```python
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i])
```

Ở đây bắt buộc cần `index`.

---

## 6. `enumerate()` — lấy cả index và value

Thay vì:

```python
for i in range(len(nums)):
    num = nums[i]
```

ta có thể viết:

```python
for i, num in enumerate(nums):
    print(i, num)
```

Ví dụ:

```python
nums = [5, 8, 12]
```

thì:

```text
i=0, num=5
i=1, num=8
i=2, num=12
```

Đây là cú pháp bạn sẽ gặp rất nhiều trong LeetCode.

Hãy hiểu:

```python
for i, num in enumerate(nums):
```

là:

> Với mỗi phần tử, lấy cho tôi cả vị trí `i` và giá trị `num`.

---

## 7. Pattern cơ bản nhất: duyệt và giữ trạng thái

Đây là một tư duy cực kỳ quan trọng.

Giả sử cần tìm số lớn nhất:

```python
nums = [4, 7, 2, 9, 5]
```

Ta không cần nhớ toàn bộ quá trình.

Chỉ cần giữ:

```text
max_so_far
```

Ví dụ:

```text
Bắt đầu:
max = 4

Đọc 7
7 > 4
→ max = 7

Đọc 2
2 < 7
→ giữ nguyên

Đọc 9
9 > 7
→ max = 9

Đọc 5
5 < 9
→ giữ nguyên
```

Đây gọi là giữ **state** khi traversal.

Pattern:

```text
Traverse Array
+
Giữ thông tin cần thiết
```

---

## 8. Tìm maximum

Cách tư duy:

```python
nums = [4, 7, 2, 9, 5]
```

Ta có thể viết:

```python
max_value = nums[0]

for num in nums:
    if num > max_value:
        max_value = num
```

Kết quả:

```text
9
```

Điều quan trọng không phải code.

Điều cần nhớ là:

```text
Đang duyệt
↓
Có giá trị tốt nhất hiện tại
↓
Nếu gặp giá trị tốt hơn
↓
Update
```

Pattern này sau này xuất hiện rất nhiều.

---

## 9. Tìm minimum

Tương tự:

```python
min_value = nums[0]

for num in nums:
    if num < min_value:
        min_value = num
```

Điểm cần chú ý:

Không nên mặc định:

```python
min_value = 0
```

Ví dụ:

```python
nums = [5, 7, 10]
```

Nếu đặt:

```python
min_value = 0
```

thì kết quả sẽ sai.

Vì `0` không tồn tại trong Array.

Do đó thường an toàn hơn:

```python
min_value = nums[0]
```

---

## 10. Tính tổng

Cho:

```python
nums = [2, 4, 6]
```

Ta giữ:

```python
total = 0
```

Duyệt:

```python
for num in nums:
    total += num
```

Dry-run:

```text
total = 0

num = 2
total = 2

num = 4
total = 6

num = 6
total = 12
```

Pattern:

```text
Accumulation
```

Hay hiểu đơn giản là:

> Duyệt tới đâu, cộng dồn tới đó.

---

## 11. Đếm số phần tử thỏa điều kiện

Ví dụ:

> Có bao nhiêu số chẵn?

```python
nums = [1, 2, 4, 7, 8]
```

Ta cần một biến:

```python
count = 0
```

Sau đó:

```python
for num in nums:
    if num % 2 == 0:
        count += 1
```

Dry-run:

```text
1 → không đếm
2 → count = 1
4 → count = 2
7 → không đếm
8 → count = 3
```

Pattern:

```text
Condition
+
Counter
```

---

## 12. Tìm một phần tử

Ví dụ:

```python
nums = [4, 8, 2, 9]
target = 2
```

Cách cơ bản:

```python
for i in range(len(nums)):
    if nums[i] == target:
        return i
```

Đây là **Linear Search**.

Worst case:

```text
target nằm cuối
```

hoặc:

```text
target không tồn tại
```

Ta phải duyệt `n` phần tử.

Time Complexity:

```text
O(n)
```

---

## 13. Khi nào dùng một loop?

Nếu đề hỏi:

- tổng
- min/max
- số lượng
- tìm phần tử
- tìm trạng thái tốt nhất
- kiểm tra điều kiện từng phần tử

thì thường nghĩ trước tới:

```text
One Pass
```

Ví dụ:

```python
for num in nums:
    ...
```

Time Complexity thường là:

```text
O(n)
```

---

## 14. Brute Force thường xuất hiện dưới dạng nested loop

Giả sử đề hỏi:

> Có hai số nào có tổng bằng `10` không?

Với:

```python
nums = [2, 4, 7, 8]
```

Cách tự nhiên nhất có thể là thử mọi cặp:

```text
2 + 4
2 + 7
2 + 8

4 + 7
4 + 8

7 + 8
```

Code kiểu:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 10:
            return True
```

Đây là Brute Force.

Nếu có `n` phần tử, số cặp có thể tăng gần theo:

```text
n²
```

Time Complexity:

```text
O(n²)
```

Đây sẽ là một câu hỏi rất quan trọng sau này:

> Có cách nào tránh loop bên trong không?

Từ câu hỏi đó chúng ta sẽ dẫn tới **Hash Map** hoặc **Two Pointers**.

---

## 15. Một lỗi rất phổ biến: nhầm index với value

Cho:

```python
nums = [10, 20, 30]
```

Đoạn:

```python
for i in nums:
```

thì `i` thực tế nhận:

```text
10
20
30
```

Không phải:

```text
0
1
2
```

Tên biến `i` không khiến nó trở thành index.

Ví dụ:

```python
for i in nums:
    print(i)
```

→

```text
10
20
30
```

Nếu muốn index:

```python
for i in range(len(nums)):
```

hoặc:

```python
for i, num in enumerate(nums):
```

---

## 16. Thay đổi Array trong lúc duyệt

Cho:

```python
nums = [1, 2, 3]
```

Ta có thể:

```python
for i in range(len(nums)):
    nums[i] = nums[i] * 2
```

Kết quả:

```python
[2, 4, 6]
```

Điều này gọi là thay đổi **in-place**.

Không tạo Array mới.

Sau này khi phân tích Space Complexity, điều này rất quan trọng.

---

## 17. Tạo Array mới

Ví dụ:

```python
nums = [1, 2, 3]
result = []

for num in nums:
    result.append(num * 2)
```

Kết quả:

```python
result = [2, 4, 6]
```

Ở đây ta tạo Array mới có `n` phần tử.

Space Complexity:

```text
O(n)
```

Trong khi sửa trực tiếp `nums` có thể chỉ cần:

```text
O(1) extra space
```

---

## 18. Time Complexity của các thao tác cơ bản

Hiện tại cần nhớ:

| Thao tác | Complexity |
|---|---:|
| `nums[i]` | `O(1)` |
| `nums[i] = x` | `O(1)` |
| duyệt toàn Array | `O(n)` |
| tìm bằng Linear Search | `O(n)` |
| nested loop trên Array | thường `O(n²)` |
| `append()` cuối list | trung bình `O(1)` |

Ví dụ:

```python
nums[5]
```

Python có thể truy cập trực tiếp vị trí đó.

→ `O(1)`.

Nhưng:

```python
for num in nums:
```

phải đi qua từng phần tử.

→ `O(n)`.

---

## 19. Space Complexity cơ bản

Ví dụ 1:

```python
total = 0

for num in nums:
    total += num
```

Ta chỉ có vài biến:

```text
total
num
```

Dù Array có 10 hay 1 triệu phần tử, số biến thêm vào không tăng đáng kể.

Extra Space:

```text
O(1)
```

Ví dụ 2:

```python
result = []

for num in nums:
    result.append(num)
```

Nếu có `n` phần tử thì `result` có thể chứa `n` phần tử.

Space Complexity:

```text
O(n)
```

---

## 20. Các dấu hiệu khi đọc đề Array

Khi đọc một bài, hãy chú ý từ khóa.

### “Maximum / Minimum”

Có thể nghĩ tới:

```text
Traversal + giữ best state
```

### “Count how many...”

Có thể nghĩ tới:

```text
Traversal + counter
```

### “Find the index...”

Có thể cần:

```text
index
range()
enumerate()
```

### “Pair”

Ví dụ:

> Find two numbers...

Hãy cảnh giác với:

```text
nested loop → O(n²)
```

Sau này có thể tối ưu bằng:

```text
Hash Map / Two Pointers
```

### “Duplicate”

Có thể nghĩ tới:

```text
Hash Set
```

### “Contiguous subarray”

Chưa học ngay, nhưng cần bắt đầu nhận diện:

```text
Sliding Window / Prefix Sum
```

---

## 21. Quy trình suy nghĩ với một bài Array

Khi gặp bài mới, không viết code ngay.

Hãy hỏi:

```text
1. Input là gì?
2. Output là gì?
3. Tôi cần value hay index?
4. Có cần duyệt toàn Array không?
5. Trong lúc duyệt, tôi cần giữ thông tin gì?
6. Có nested loop không?
7. Nếu có, có tránh được không?
```

Đây là nền tảng của tư duy thuật toán.

---

## 22. Ví dụ suy luận nhỏ

Cho:

```python
nums = [3, 8, 2, 10, 5]
```

Yêu cầu:

> Tìm số lớn nhất.

Ta suy nghĩ:

```text
Input
→ Array

Output
→ một số

Có cần tất cả index?
→ Không

Có cần xem mỗi phần tử?
→ Có

Cần giữ gì?
→ số lớn nhất đã thấy

Pattern
→ One Pass + State
```

Do đó:

```text
O(n)
```

Không cần:

```text
O(n²)
```

---

## 23. Pattern cần ghi nhớ sau bài này

### Pattern 1

```text
Array
+
tìm min/max
→ One Pass + Best State
```

### Pattern 2

```text
Array
+
count theo điều kiện
→ One Pass + Counter
```

### Pattern 3

```text
Array
+
tính tổng
→ One Pass + Accumulator
```

### Pattern 4

```text
Pair
+
Brute Force
→ thường Nested Loop O(n²)
```

### Pattern 5

```text
Need index
→ range() / enumerate()
```

---

## 24. Những lỗi cần tránh

### Lỗi 1 — vượt index

Sai:

```python
for i in range(len(nums) + 1):
```

Nếu truy cập:

```python
nums[i]
```

có thể lỗi.

### Lỗi 2 — nhầm value với index

```python
for i in nums:
```

`i` là value.

### Lỗi 3 — khởi tạo max/min sai

Không nên luôn dùng:

```python
max_value = 0
```

Vì Array có thể:

```python
[-10, -5, -2]
```

Nếu vậy `0` sẽ làm kết quả sai.

### Lỗi 4 — dùng nested loop khi không cần

Ví dụ tìm maximum không cần:

```python
for i ...
    for j ...
```

Chỉ cần một traversal.

---

# Kiểm tra nhanh

Trả lời theo suy nghĩ, chưa cần viết solution hoàn chỉnh.

### Câu 1

Cho:

```python
nums = [6, 3, 9, 2]
```

Giá trị của:

```python
nums[len(nums) - 1]
```

là bao nhiêu?

### Câu 2

Đoạn này duyệt theo **index** hay **value**?

```python
for num in nums:
    print(num)
```

### Câu 3

Nếu muốn tìm số lớn nhất trong Array, trong lúc duyệt ta nên giữ biến gì?

- **A.** `count`
- **B.** `max_so_far`
- **C.** `index_list`

### Câu 4

Đoạn code:

```python
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])
```

Time Complexity là:

- **A.** `O(1)`
- **B.** `O(n)`
- **C.** `O(n²)`

### Câu 5

Nếu tạo:

```python
result = []
```

và thêm vào `result` khoảng `n` phần tử, extra Space Complexity thường là gì?

- **A.** `O(1)`
- **B.** `O(n)`
- **C.** `O(n²)`

Trả lời theo dạng:

```text
1. ...
2. ...
3. ...
4. ...
5. ...
```

Sau phần này, bài thực hành đầu tiên phù hợp sẽ là **LeetCode 1480 — Running Sum of 1d Array**, vì bài đó luyện đúng ba thứ vừa học: **Array traversal + accumulator + Time/Space Complexity**.
