# Bài lý thuyết 3/10 — Hash Map / Hash Set

## Mục tiêu

Sau bài này, bạn cần hiểu:

- Hash Map và Hash Set là gì.
- Khi nào dùng `dict`, khi nào dùng `set`.
- Tại sao lookup trung bình có thể là `O(1)`.
- Pattern Duplicate, Frequency, Pair + Target.
- Cách dùng `get()`, `in`, `add()`.
- Cách biến Brute Force `O(n²)` thành `O(n)` trong nhiều bài.

---

## 1. Hash Map là gì?

Trong Python, Hash Map thường là `dict`.

```python
student = {
    "name": "An",
    "age": 18
}
```

Nó lưu:

```text
key → value
```

Ví dụ:

```python
student["name"]
```

→ `"An"`

Trong LeetCode, ta thường lưu kiểu:

```text
number → index
character → count
value → metadata
```

---

## 2. Hash Set là gì?

Trong Python:

```python
seen = set()
```

Set chỉ lưu các giá trị duy nhất.

```python
seen.add(5)
seen.add(5)
```

Kết quả vẫn chỉ có:

```text
{5}
```

Set rất phù hợp với câu hỏi:

> Giá trị này đã xuất hiện chưa?

---

## 3. `dict` và `set` khác nhau thế nào?

`dict`:

```text
key → value
```

Ví dụ:

```python
freq = {
    "a": 3,
    "b": 1
}
```

`set`:

```text
chỉ lưu key
```

Ví dụ:

```python
seen = {"a", "b"}
```

Quy tắc đơn giản:

```text
Chỉ cần biết tồn tại hay không
→ set
```

```text
Cần gắn thêm thông tin
→ dict
```

---

## 4. Membership lookup

Với list:

```python
x in nums
```

Worst case có thể phải duyệt toàn bộ Array.

→ `O(n)`

Với Hash Set:

```python
x in seen
```

trung bình:

→ `O(1)`

Với Hash Map:

```python
x in mapping
```

trung bình:

→ `O(1)`

Đây là lý do Hash Map / Hash Set rất mạnh.

---

## 5. Pattern Duplicate

Cho:

```python
nums = [1, 2, 3, 1]
```

Câu hỏi:

> Có duplicate không?

Brute Force:

```text
so sánh mọi cặp
→ O(n²)
```

Tốt hơn:

```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)
```

Pattern:

```text
Duplicate
→ Hash Set
```

---

## 6. Pattern Frequency

Cho:

```python
nums = [1, 2, 1, 3, 1]
```

Ta muốn:

```text
1 → 3
2 → 1
3 → 1
```

Dùng:

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

`get()` hoạt động như:

```python
freq.get(num, 0)
```

nghĩa là:

> Nếu `num` tồn tại thì lấy value, nếu chưa tồn tại thì dùng `0`.

Pattern:

```text
Frequency / Count
→ Hash Map
```

---

## 7. Pair + Target

Đây là pattern cực kỳ quan trọng.

Ví dụ:

```python
nums = [2, 7, 11, 15]
target = 9
```

Ta cần tìm:

```text
2 + 7 = 9
```

Brute Force:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
```

→ `O(n²)`

Nhưng khi đang đứng tại `num`, ta có thể hỏi:

```text
Tôi còn thiếu số nào?
```

Công thức:

```text
needed = target - num
```

Nếu `needed` đã xuất hiện trước đó, ta tìm được pair.

Đây chính là nền tảng của Two Sum.

Pattern:

```text
Pair + Target
→ Hash Map
```

---

## 8. Tại sao cần Hash Map thay vì Hash Set trong Two Sum?

Nếu chỉ cần:

> Có pair hay không?

Hash Set có thể đủ.

Nhưng nếu đề yêu cầu:

> Trả về index của hai số.

Ta cần lưu:

```text
value → index
```

Ví dụ:

```python
seen = {
    2: 0,
    7: 1
}
```

Do đó cần `dict`.

---

## 9. Các thao tác `dict` quan trọng

Tạo:

```python
mapping = {}
```

Gán:

```python
mapping[10] = 3
```

Đọc:

```python
mapping[10]
```

Kiểm tra:

```python
10 in mapping
```

Dùng `get()`:

```python
mapping.get(10, 0)
```

---

## 10. Các thao tác `set` quan trọng

Tạo:

```python
seen = set()
```

Thêm:

```python
seen.add(10)
```

Kiểm tra:

```python
10 in seen
```

Xóa:

```python
seen.remove(10)
```

Trong Sliding Window sau này, việc thêm/xóa trong set rất thường gặp.

---

## 11. Hash Map như memory

Một cách hiểu quan trọng:

> Hash Map là bộ nhớ của những gì ta đã thấy.

Ví dụ:

```text
Duyệt Array
↓
gặp num
↓
lưu num
↓
các bước sau có thể hỏi lại rất nhanh
```

Tư duy này sẽ xuất hiện trong:

- Two Sum
- Frequency
- Prefix Sum + Hash Map
- Sliding Window
- nhiều bài Medium

---

## 12. Brute Force → Optimization

Một pattern suy luận rất quan trọng:

```text
Brute Force:
mỗi phần tử phải tìm một thứ khác trong Array
↓
search đó mất O(n)
↓
nested effect → O(n²)
↓
có thể lưu thứ đã thấy trong Hash Map/Set không?
↓
lookup O(1)
↓
tổng thể có thể xuống O(n)
```

Đây là một trong những kỹ năng quan trọng nhất của roadmap.

---

## 13. Space Complexity

Hash Set:

```python
seen = set()
```

Nếu lưu tối đa `n` phần tử:

→ `O(n)` space.

Hash Map:

```python
mapping = {}
```

Nếu lưu tối đa `n` key:

→ `O(n)` space.

Đây là trade-off:

```text
Dùng thêm memory
→ giảm Time Complexity
```

---

## 14. Khi nào nghĩ đến Hash Map / Hash Set?

### Duplicate

```text
"Have I seen this before?"
→ Hash Set
```

### Frequency

```text
"How many times?"
→ Hash Map
```

### Pair + Target

```text
"What complement do I need?"
→ Hash Map
```

### Mapping

```text
"Value này liên kết với thông tin gì?"
→ Hash Map
```

---

## 15. Một lỗi thường gặp

### Lỗi 1: thêm vào `seen` quá sớm

Trong bài Pair + Target, thứ tự:

```text
check trước
rồi mới add
```

thường rất quan trọng.

Nếu add trước, có thể vô tình dùng chính phần tử hiện tại.

---

### Lỗi 2: nhầm key và value

```python
mapping[value] = index
```

thì:

```text
key = value
value của dict = index
```

Cần luôn biết mình đang lưu chiều nào.

---

### Lỗi 3: dùng list thay set cho membership nhiều lần

Ví dụ:

```python
if num in nums_seen:
```

nếu `nums_seen` là list thì lookup `O(n)`.

Nếu lặp lại bên trong loop, có thể thành `O(n²)`.

---

## 16. Complexity cần nhớ

| Thao tác | Average Time |
|---|---:|
| `x in set` | `O(1)` |
| `set.add(x)` | `O(1)` |
| `key in dict` | `O(1)` |
| `dict[key]` | `O(1)` |
| duyệt `n` phần tử | `O(n)` |

---

## 17. Kiểm tra nhanh

### Câu 1

Nếu chỉ cần kiểm tra duplicate, nên ưu tiên:

- A. `set`
- B. `dict`
- C. `list`

### Câu 2

Nếu cần đếm frequency, nên ưu tiên:

- A. `set`
- B. `dict`

### Câu 3

Trong bài Pair + Target, với `num`, ta thường tính:

```text
needed = ?
```

### Câu 4

Nếu duyệt Array một lần và mỗi bước lookup Hash Map trung bình `O(1)`, tổng Time Complexity thường là:

- A. `O(1)`
- B. `O(n)`
- C. `O(n²)`

### Câu 5

Hash Map có thể dùng thêm `O(n)` space để giảm thời gian từ `O(n²)` xuống `O(n)`. Đúng hay sai?

---

## Pattern cần ghi nhớ

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
→ Hash Map
```

```text
Need value → index mapping
→ Hash Map
```
