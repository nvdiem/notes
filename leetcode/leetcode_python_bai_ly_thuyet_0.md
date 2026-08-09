# Bài lý thuyết 0/10 — Python nền tảng cho LeetCode

Mục tiêu của bài này: đủ Python để bắt đầu giải Array. Chưa cần học Python quá sâu.

## 1. `list` — cấu trúc dùng nhiều nhất

Trong LeetCode, Array thường được biểu diễn bằng `list`.

```python
nums = [10, 20, 30, 40]
```

Mỗi phần tử có một **index**:

```text
Value:  10  20  30  40
Index:   0   1   2   3
```

Truy cập phần tử:

```python
nums[0]   # 10
nums[2]   # 30
```

Phần tử cuối:

```python
nums[-1]  # 40
```

Điểm cần nhớ:

> Python bắt đầu index từ `0`.

---

## 2. `len()` — lấy số phần tử

```python
nums = [10, 20, 30, 40]

print(len(nums))
```

Kết quả:

```text
4
```

Nếu:

```python
n = len(nums)
```

thì index hợp lệ là:

```text
0 → n - 1
```

Không phải:

```text
0 → n
```

Ví dụ:

```python
nums[len(nums)]
```

sẽ lỗi:

```text
IndexError
```

Đây là lỗi rất thường gặp khi làm LeetCode.

---

## 3. Duyệt Array bằng `for`

Cách đơn giản nhất:

```python
nums = [10, 20, 30]

for num in nums:
    print(num)
```

Ta nhận được:

```text
10
20
30
```

Ở đây:

```python
num
```

là **value**, không phải index.

### Khi cần index

Ta có thể dùng:

```python
for i in range(len(nums)):
    print(i, nums[i])
```

Kết quả:

```text
0 10
1 20
2 30
```

Hình dung:

```text
i = 0 → nums[0] = 10
i = 1 → nums[1] = 20
i = 2 → nums[2] = 30
```

---

## 4. `range()`

Đây là cú pháp rất quan trọng.

```python
range(5)
```

tạo ra:

```text
0, 1, 2, 3, 4
```

Không có `5`.

Do đó:

```python
for i in range(len(nums)):
```

nếu `len(nums) = 4` thì:

```text
i = 0, 1, 2, 3
```

vừa đúng với index của Array.

### Một số dạng khác

```python
range(2, 5)
```

→

```text
2, 3, 4
```

Hoặc:

```python
range(5, 0, -1)
```

→

```text
5, 4, 3, 2, 1
```

---

## 5. `enumerate()` — cực kỳ hữu ích

Thay vì:

```python
for i in range(len(nums)):
    num = nums[i]
```

Python cho phép:

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

> "Cho tôi cả **index** và **value**."

---

## 6. Thay đổi phần tử trong Array

```python
nums = [10, 20, 30]

nums[1] = 100
```

Kết quả:

```python
[10, 100, 30]
```

Đây là điểm khác với String.

`list` có thể thay đổi trực tiếp.

---

## 7. `append()`

Thêm phần tử vào cuối:

```python
nums = []

nums.append(10)
nums.append(20)
```

Kết quả:

```python
[10, 20]
```

Rất nhiều solution LeetCode có dạng:

```python
result = []

for num in nums:
    if ...:
        result.append(num)
```

---

## 8. `dict` — Hash Map

Một `dict` lưu dữ liệu theo dạng:

```text
key → value
```

Ví dụ:

```python
student = {
    "name": "An",
    "age": 18
}
```

Truy cập:

```python
student["name"]
```

→

```text
"An"
```

Trong LeetCode, thường không phải lưu tên học sinh mà dùng kiểu:

```python
frequency = {}
```

Ví dụ đếm số:

```python
nums = [1, 2, 1]
```

Ta muốn:

```text
1 → 2 lần
2 → 1 lần
```

Hash Map:

```python
{
    1: 2,
    2: 1
}
```

---

## 9. `set` — Hash Set

`set` chỉ quan tâm:

> phần tử có tồn tại hay không.

Ví dụ:

```python
seen = set()

seen.add(5)
seen.add(10)
```

Kiểm tra:

```python
5 in seen
```

→

```text
True
```

Điểm đặc biệt:

```python
seen.add(5)
seen.add(5)
```

vẫn chỉ có:

```python
{5}
```

Vì `set` không lưu duplicate.

Do đó khi đề nói:

> Có phần tử nào bị lặp không?

hãy bắt đầu nghĩ tới:

**Hash Set**.

---

## 10. `in` — cú pháp cực kỳ quan trọng

Ví dụ:

```python
nums = [10, 20, 30]

20 in nums
```

→ `True`

Nhưng có một vấn đề thuật toán quan trọng.

Với `list`:

```python
x in nums
```

có thể phải tìm lần lượt:

```text
10
↓
20
↓
30
↓
...
```

Time Complexity:

```text
O(n)
```

Trong khi với:

```python
x in seen
```

với `seen` là `set`, trung bình là:

```text
O(1)
```

Đây chính là một trong những lý do **Hash Set / Hash Map** mạnh.

---

## 11. Time Complexity cơ bản

Bạn chưa cần thuộc mọi complexity.

Hiện tại chỉ cần phân biệt 4 mức:

```text
O(1)
O(log n)
O(n)
O(n²)
```

### `O(1)`

Số phần tử tăng nhưng số thao tác gần như không đổi.

```python
nums[0]
```

### `O(n)`

Duyệt toàn bộ Array một lần:

```python
for num in nums:
    print(num)
```

Nếu Array có `n` phần tử:

```text
n phần tử
→ khoảng n lần xử lý
```

→ `O(n)`.

### `O(n²)`

Nested loop:

```python
for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])
```

Nếu:

```text
n = 100
```

thì có thể khoảng:

```text
100 × 100 = 10,000
```

operations.

→ `O(n²)`.

Đây sẽ là nguồn gốc của rất nhiều **Brute Force solution**.

---

## 12. Một ví dụ quan trọng

Cho:

```python
nums = [2, 7, 11, 15]
```

Tìm xem có số `7` không.

### Cách 1

```python
for num in nums:
    if num == 7:
        return True
```

Time Complexity:

```text
O(n)
```

### Cách 2

Nếu trước đó ta đã xây `set`:

```python
seen = {2, 7, 11, 15}

return 7 in seen
```

Lookup trung bình:

```text
O(1)
```

Đây là tư duy chúng ta sẽ dùng rất nhiều:

```text
Tìm kiếm chậm
↓
Có thể lưu thông tin trước không?
↓
Hash Map / Hash Set
```

---

# Những cú pháp cần nhớ sau bài này

```python
nums = [1, 2, 3]

len(nums)

nums[0]

for num in nums:
    ...

for i in range(len(nums)):
    ...

for i, num in enumerate(nums):
    ...

nums.append(10)

d = {}

s = set()

s.add(10)

10 in s
```

Bạn **không cần học thuộc code**. Chỉ cần hiểu mỗi câu đang làm gì.

---

# Pattern đầu tiên cần ghi nhớ

Hai dấu hiệu đầu tiên:

```text
Duplicate
→ Hash Set
```

và:

```text
Frequency / Count
→ Hash Map
```

Chúng ta sẽ gặp lại hai pattern này nhiều lần.

---

## Kiểm tra nhanh

Chưa cần viết code. Trả lời bằng suy nghĩ của bạn:

### Câu 1

```python
nums = [5, 8, 10, 12]
```

`nums[2]` bằng bao nhiêu?

### Câu 2

```python
for i in range(4):
```

`i` lần lượt nhận những giá trị nào?

### Câu 3

Nếu đề bài hỏi:

> "Array có phần tử nào xuất hiện hai lần không?"

Bạn nghĩ cấu trúc nào phù hợp hơn?

- **A.** `list`
- **B.** `set`

### Câu 4

Đoạn code sau có Time Complexity là gì?

```python
for num in nums:
    print(num)
```

- **A.** `O(1)`
- **B.** `O(n)`
- **C.** `O(n²)`

Bạn có thể trả lời dạng:

```text
1. ...
2. ...
3. ...
4. ...
```

Sau khi kiểm tra 4 câu này, chúng ta sẽ chuyển sang **Bài lý thuyết 1/10 — Array 1D**, rồi bắt đầu bài LeetCode đầu tiên.
