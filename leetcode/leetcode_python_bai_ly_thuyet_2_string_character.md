# Bài lý thuyết 2/10 — String & Character

## Mục tiêu

Sau bài này, bạn cần hiểu:

- String là chuỗi ký tự.
- Cách truy cập từng character bằng index.
- String là immutable.
- Cách duyệt String.
- Các thao tác thường gặp: `lower()`, `upper()`, slicing.
- `ord()` và `chr()`.
- Cách nhận diện bài Palindrome, Frequency, Anagram.
- Time Complexity cơ bản khi xử lý String.

---

## 1. String là gì?

```python
s = "hello"
```

Ta có thể hình dung:

```text
Character: h e l l o
Index:     0 1 2 3 4
```

Truy cập:

```python
s[0]   # 'h'
s[4]   # 'o'
s[-1]  # 'o'
```

---

## 2. Character trong Python

Python không có kiểu `char` riêng như một số ngôn ngữ khác.

Một character đơn giản là String có độ dài 1:

```python
ch = "a"
```

```python
len(ch)  # 1
```

---

## 3. Duyệt String

Theo value:

```python
for ch in s:
    print(ch)
```

Theo index:

```python
for i in range(len(s)):
    print(i, s[i])
```

Cả index và value:

```python
for i, ch in enumerate(s):
    print(i, ch)
```

---

## 4. String là immutable

Với list:

```python
nums = [1, 2, 3]
nums[0] = 100
```

Được phép.

Nhưng với String:

```python
s = "cat"
s[0] = "b"
```

sẽ lỗi.

Ta phải tạo String mới:

```python
s = "b" + s[1:]
```

Kết quả:

```text
bat
```

---

## 5. `lower()` và `upper()`

```python
s = "Hello"

s.lower()  # "hello"
s.upper()  # "HELLO"
```

Rất hữu ích khi đề yêu cầu:

> Ignore uppercase/lowercase.

Ví dụ:

```python
"A".lower() == "a"
```

→ `True`

---

## 6. Slicing

```python
s = "python"
```

```python
s[1:4]
```

→

```text
yth
```

Quy tắc:

```text
[start : end]
```

lấy `start`, không lấy `end`.

Đảo String:

```python
s[::-1]
```

→

```text
nohtyp
```

Slicing tiện, nhưng khi học thuật toán ta vẫn cần hiểu Two Pointers thay vì chỉ dựa vào `[::-1]`.

---

## 7. `ord()` và `chr()`

`ord()` biến character thành mã số:

```python
ord("a")  # 97
ord("b")  # 98
```

`chr()` làm ngược lại:

```python
chr(97)  # 'a'
```

Ứng dụng:

```python
ord("c") - ord("a")
```

→ `2`

Tức là `'c'` cách `'a'` hai vị trí.

---

## 8. Kiểm tra ký tự

Một số method hữu ích:

```python
ch.isalpha()
ch.isdigit()
ch.isalnum()
```

Ví dụ:

```python
"a".isalpha()   # True
"5".isdigit()   # True
"a".isalnum()   # True
```

Rất hay gặp trong bài xử lý String.

---

## 9. Frequency của Character

Cho:

```python
s = "aabcc"
```

Ta muốn:

```text
a → 2
b → 1
c → 2
```

Có thể dùng Hash Map:

```python
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
```

Pattern:

```text
Character Frequency
→ Hash Map
```

---

## 10. Duplicate Character

Ví dụ:

```python
s = "hello"
```

Nếu cần kiểm tra có ký tự lặp không:

```python
seen = set()

for ch in s:
    if ch in seen:
        return True
    seen.add(ch)
```

Pattern:

```text
Duplicate
→ Hash Set
```

---

## 11. Palindrome

Palindrome là chuỗi đọc xuôi và ngược giống nhau.

Ví dụ:

```text
racecar
level
madam
```

Dấu hiệu:

```text
Palindrome
→ Two Pointers
```

Hình dung:

```text
r a c e c a r
↑           ↑
left      right
```

Ta so sánh hai đầu rồi tiến dần vào giữa.

---

## 12. Anagram

Hai String là Anagram nếu chứa cùng các ký tự với cùng số lần xuất hiện.

Ví dụ:

```text
"anagram"
"nagaram"
```

Pattern thường dùng:

```text
Frequency
→ Hash Map
```

Hoặc dùng `Counter`.

---

## 13. `Counter`

Python có:

```python
from collections import Counter
```

Ví dụ:

```python
Counter("aabcc")
```

tương đương:

```python
{
    "a": 2,
    "b": 1,
    "c": 2
}
```

Trong LeetCode, `Counter` rất tiện, nhưng bạn vẫn nên hiểu bản chất Hash Map.

---

## 14. Time Complexity cơ bản

Duyệt String một lần:

```python
for ch in s:
```

→ `O(n)`

Nested loop:

```python
for i in range(len(s)):
    for j in range(len(s)):
```

→ `O(n²)`

Kiểm tra membership trong `set` trung bình:

```python
ch in seen
```

→ `O(1)`

---

## 15. Các dấu hiệu cần nhớ

```text
Palindrome
→ Two Pointers
```

```text
Frequency
→ Hash Map
```

```text
Duplicate
→ Hash Set
```

```text
Same characters / Anagram
→ Frequency
```

```text
Ignore uppercase/lowercase
→ lower() / upper()
```

---

## 16. Kiểm tra nhanh

### Câu 1

```python
s = "python"
```

`s[2]` là gì?

### Câu 2

String có sửa trực tiếp `s[i]` được không?

### Câu 3

Nếu đề yêu cầu đếm số lần mỗi character xuất hiện, pattern nào phù hợp?

- A. Hash Map
- B. Binary Search
- C. Prefix Sum

### Câu 4

Palindrome thường gợi ý pattern nào?

- A. Two Pointers
- B. BFS
- C. Prefix Sum

### Câu 5

Duyệt toàn bộ String một lần có Time Complexity là gì?

- A. `O(1)`
- B. `O(n)`
- C. `O(n²)`

---

## Pattern cần ghi nhớ

```text
String
→ duyệt character
```

```text
Palindrome
→ Two Pointers
```

```text
Frequency / Anagram
→ Hash Map
```

```text
Duplicate
→ Hash Set
```
