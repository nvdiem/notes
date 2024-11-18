#BAI 1: Sinh dãy nhị phân độ dài n
#===Begin===
x = [0] * 100  # Mảng để lưu dãy nhị phân
n = int(input("Nhập n: "))  # Độ dài của dãy nhị phân

def print_result():
    """Hàm in ra dãy nhị phân hiện tại"""
    for i in range(1, n + 1):
        print(x[i], end="")
    print()

def Try(i):
    """Hàm đệ quy để sinh dãy nhị phân"""
    for j in range(2):  # j chạy từ 0 đến 1
        x[i] = j
        if i == n:
            print_result()  # Nếu đã điền đủ n phần tử, in kết quả
        else:
            Try(i + 1)  # Sinh tiếp dãy nhị phân từ vị trí i+1

# Gọi hàm Try để bắt đầu sinh dãy từ vị trí 1
Try(1)
#===!End===

#BAI 2: Sinh dãy ký tự "A" và "B" có độ dài n
#===Begin===
x = [''] * 100  # Mảng để lưu dãy ký tự
n = int(input("Nhập n: "))  # Độ dài của dãy ký tự

def print_result():
    """Hàm in ra dãy ký tự hiện tại"""
    for i in range(1, n + 1):
        print(x[i], end="")
    print()

def Try(i):
    """Hàm đệ quy để sinh dãy ký tự 'A' và 'B'"""
    for j in ['A', 'B']:  # j chạy qua 2 giá trị 'A' và 'B'
        x[i] = j
        if i == n:
            print_result()  # Nếu đã điền đủ n phần tử, in kết quả
        else:
            Try(i + 1)  # Sinh tiếp dãy ký tự từ vị trí i+1

# Gọi hàm Try để bắt đầu sinh dãy từ vị trí 1
Try(1)
#===!End===

#BÀI 3: Chương trình sinh tổ hợp chập k của n
# Chương trình sinh tổ hợp chập k của n
#===Begin===
x = [0] * 100  # Mảng để lưu tổ hợp hiện tại
n = int(input("Nhập n: "))  # Tổng số phần tử
k = int(input("Nhập k: "))  # Số phần tử trong mỗi tổ hợp

def print_result():
    """Hàm in ra tổ hợp hiện tại"""
    for i in range(1, k + 1):
        print(x[i], end=" ")
    print()

def Try(i):
    """Hàm đệ quy để sinh tổ hợp chập k của n"""
    # Nếu đã chọn đủ k phần tử thì in ra tổ hợp
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            print_result()
        else:
            Try(i + 1)

# Bắt đầu sinh tổ hợp từ vị trí 1
x[0] = 0  # Khởi tạo giá trị ban đầu
Try(1)
#===!End===

#BÀI 4: Chương trình sinh hoán vị
#===Begin===
# Hàm sinh hoán vị của n phần tử
n = int(input("Nhập n: "))  # Số lượng phần tử
x = [0] * (n + 1)           # Mảng để lưu các hoán vị
used = [False] * (n + 1)    # Mảng đánh dấu các phần tử đã sử dụng

def print_result():
    """Hàm in ra hoán vị hiện tại"""
    for i in range(1, n + 1):
        print(x[i], end=" ")
    print()

def Try(i):
    """Hàm đệ quy sinh hoán vị"""
    for j in range(1, n + 1):
        if not used[j]:
            x[i] = j        # Chọn phần tử j cho vị trí i
            used[j] = True  # Đánh dấu j đã được sử dụng
            if i == n:
                print_result()  # In kết quả khi đủ n phần tử
            else:
                Try(i + 1)  # Đệ quy cho vị trí tiếp theo
            used[j] = False # Bỏ đánh dấu để thử hoán vị khác

# Bắt đầu sinh hoán vị từ vị trí 1
Try(1)

#===End===

#===Begin===
#Bài 6. Dãy con có tổng bằng K
def Try(i, pos):
    global sum, found
    for j in range(pos - 1, n):  # Chỉnh sửa: bắt đầu từ `pos - 1` vì Python dùng chỉ số từ 0
        X[i] = A[j]
        sum += A[j]
        # Nếu tổng hiện tại bằng K, in ra dãy con
        if sum == K:
            found = True
            print('[', ' '.join(map(str, X[1:i + 1])), ']', sep="")
        else:
            # Gọi đệ quy để tiếp tục tìm dãy con
            Try(i + 1, j + 2)  # Chỉnh sửa: truyền `j + 2` để duyệt từ phần tử tiếp theo
        # Quay lui, loại bỏ phần tử vừa thêm
        sum -= A[j]

# Đọc số lượng bộ test
T = int(input("Nhập số lượng bộ test: "))

for _ in range(T):
    # Đọc N và K
    n, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()  # Sắp xếp để đảm bảo thứ tự từ điển
    
    X = [0] * (n + 1)  # Mảng để lưu dãy con hiện tại, bắt đầu từ chỉ số 1
    sum = 0            # Tổng của dãy con hiện tại
    found = False      # Biến để kiểm tra có dãy con nào thỏa mãn hay không

    # Gọi hàm đệ quy để tìm dãy con, bắt đầu từ `Try(1, 1)`
    Try(1, 1)

    # Nếu không tìm thấy dãy con nào, in -1
    if not found:
        print(-1)
#end 

#Bài 5. Di chuyển trong mê cung
#Begin
def Try(i, j):
    global s, found
    # Nếu đến ô (n-1, n-1), in ra đường đi và đánh dấu đã tìm thấy đường
    if i == n - 1 and j == n - 1:
        found = True
        print(s)
        return

    # Kiểm tra và di chuyển sang phải (R)
    if j + 1 < n and maze[i][j + 1] == 1:
        s += "R"  # Thêm 'R' vào chuỗi đường đi
        maze[i][j + 1] = 0  # Đánh dấu ô đã đi qua
        Try(i, j + 1)  # Gọi đệ quy để tiếp tục tìm đường
        s = s[:-1]  # Quay lui (xóa 'R' khỏi chuỗi)
        maze[i][j + 1] = 1  # Bỏ đánh dấu để thử lại sau

    # Kiểm tra và di chuyển xuống dưới (D)
    if i + 1 < n and maze[i + 1][j] == 1:
        s += "D"  # Thêm 'D' vào chuỗi đường đi
        maze[i + 1][j] = 0  # Đánh dấu ô đã đi qua
        Try(i + 1, j)  # Gọi đệ quy để tiếp tục tìm đường
        s = s[:-1]  # Quay lui (xóa 'D' khỏi chuỗi)
        maze[i + 1][j] = 1  # Bỏ đánh dấu để thử lại sau

# Đọc số lượng bộ test
T = int(input("Nhập số lượng bộ test: "))

for _ in range(T):
    # Đọc kích thước mê cung
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]

    # Chuỗi lưu đường đi
    s = ""
    found = False  # Biến để kiểm tra có tìm thấy đường đi không

    # Kiểm tra nếu ô bắt đầu hoặc ô kết thúc không khả thi
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        print(-1)
    else:
        # Bắt đầu tìm đường đi từ ô (0, 0)
        maze[0][0] = 0  # Đánh dấu ô bắt đầu đã đi qua
        Try(0, 0)

        # Nếu không tìm thấy đường đi nào, in -1
        if not found:
            print(-1)
#Bài 10. Di chuyển trong mê cung 2
#Begin            
def Try(i, j):
    global s, found
    # Nếu đã đến ô (n-1, n-1), in ra đường đi và đánh dấu đã tìm thấy đường
    if i == n - 1 and j == n - 1:
        found = True
        print(s, end=" ")
        return

    # Di chuyển xuống dưới (D)
    if i + 1 < n and maze[i + 1][j] == 1:
        s += "D"
        maze[i + 1][j] = 0  # Đánh dấu ô đã đi qua
        Try(i + 1, j)
        maze[i + 1][j] = 1  # Bỏ đánh dấu sau khi quay lui
        s = s[:-1]  # Quay lui (xóa 'D' khỏi chuỗi)

    # Di chuyển sang trái (L)
    if j - 1 >= 0 and maze[i][j - 1] == 1:
        s += "L"
        maze[i][j - 1] = 0
        Try(i, j - 1)
        maze[i][j - 1] = 1
        s = s[:-1]

    # Di chuyển sang phải (R)
    if j + 1 < n and maze[i][j + 1] == 1:
        s += "R"
        maze[i][j + 1] = 0
        Try(i, j + 1)
        maze[i][j + 1] = 1
        s = s[:-1]

    # Di chuyển lên trên (U)
    if i - 1 >= 0 and maze[i - 1][j] == 1:
        s += "U"
        maze[i - 1][j] = 0
        Try(i - 1, j)
        maze[i - 1][j] = 1
        s = s[:-1]

# Đọc số lượng bộ test
T = int(input("Nhập số lượng bộ test: "))

for _ in range(T):
    n = int(input("Nhập kích thước mê cung: "))
    maze = [list(map(int, input().split())) for _ in range(n)]

    s = ""
    found = False  # Biến để kiểm tra có đường đi nào không

    # Kiểm tra nếu ô bắt đầu và ô kết thúc đều có giá trị 1
    if maze[0][0] == 1 and maze[n - 1][n - 1] == 1:
        maze[0][0] = 0  # Đánh dấu ô bắt đầu
        Try(0, 0)

    # Nếu không tìm thấy đường đi nào, in -1
    if not found:
        print(-1)
    else:
        print()

#End

# Bài toán đếm thành phần liên thông
def inp():
    global n, maze
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]

def Try(i, j):
    maze[i][j] = 0  # Đánh dấu ô hiện tại là đã thăm
    # Các hướng di chuyển: xuống, trái, phải, lên
    dx = [1, 0, 0, -1]
    
    dy = [0, -1, 1, 0]
    
    
    for k in range(4):
        i1 = i + dx[k]
        j1 = j + dy[k]
        if 0 <= i1 < n and 0 <= j1 < n and maze[i1][j1] == 1:
            Try(i1, j1)

# Đọc số lượng bộ test
t = int(input())
for _ in range(t):
    inp()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 1:
                cnt += 1
                Try(i, j)
    print(cnt)
#End

# Bài 18 Tư điển
#Begin
# Đọc số lượng bộ test
T = int(input())

# 8 hướng di chuyển: trên, dưới, trái, phải và 4 hướng chéo
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def Try(i, j):
    global current_word, visited, result
    # Nếu từ hiện tại có trong từ điển và chưa được lưu vào kết quả, thêm vào
    if current_word in dictionary:
        result.add(current_word)
    
    # Duyệt qua 8 hướng
    for k in range(8):
        ni, nj = i + dx[k], j + dy[k]
        # Kiểm tra điều kiện biên và ô chưa được thăm
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            # Thêm ký tự vào từ hiện tại
            current_word += board[ni][nj]
            visited[ni][nj] = True
            Try(ni, nj)
            # Quay lui: bỏ ký tự cuối cùng và đánh dấu lại ô chưa thăm
            visited[ni][nj] = False
            current_word = current_word[:-1]

for _ in range(T):
    # Đọc K, M, N
    k, n, m = map(int, input().split())

    # Đọc từ điển
    dictionary = set(input().split())

    # Đọc ma trận ký tự
    board = [input().split() for _ in range(n)]

    # Khởi tạo biến lưu kết quả và visited
    result = set()
    visited = [[False] * m for _ in range(n)]

    # Tìm kiếm từ mỗi ô trong ma trận
    for i in range(n):
        for j in range(m):
            current_word = board[i][j]
            visited[i][j] = True
            Try(i, j)
            visited[i][j] = False

    # In kết quả theo thứ tự từ điển
    if not result:
        print(-1)
    else:
        sorted_result = sorted(result)
        print(" ".join(sorted_result))

#end

#Bài 9. Bài toán N quân hậu

#Begin#
def ktao():
    """Khởi tạo các mảng đánh dấu."""
    global cot, d1, d2
    cot = [0] * (n + 1)
    d1 = [0] * (2 * n)     # Đánh dấu đường chéo từ trên trái xuống dưới phải
    d2 = [0] * (2 * n)     # Đánh dấu đường chéo từ trên phải xuống dưới trái

def Try(i):
    """Hàm quay lui để đặt quân hậu."""
    global count
    if i > n:  # Nếu đã đặt đủ n quân hậu
        count += 1
        return

    # Thử đặt quân hậu ở hàng thứ i, cột j
    for j in range(1, n + 1):
        if cot[j] == 0 and d1[i - j + n] == 0 and d2[i + j - 1] == 0:
            # Đặt quân hậu vào vị trí (i, j)
            cot[j] = 1
            d1[i - j + n] = 1
            d2[i + j - 1] = 1

            # Gọi đệ quy để đặt quân hậu tiếp theo
            Try(i + 1)

            # Quay lui (backtrack)
            cot[j] = 0
            d1[i - j + n] = 0
            d2[i + j - 1] = 0

# Đọc số lượng bộ test
T = int(input("Nhập số lượng bộ test: "))
for _ in range(T):
    n = int(input("Nhập kích thước bàn cờ: "))
    count = 0
    ktao()
    Try(1)
    print(count)
#End#

#Bài 13. Bài toán N quân hậu 2
#begin
def ktao():
    """Khởi tạo bàn cờ và đọc giá trị."""
    global board
    board = [list(map(int, input().split())) for _ in range(8)]

def Try(i):
    """Hàm quay lui để đặt quân hậu."""
    global res, current_sum
    if i > 8:  # Nếu đã đặt đủ 8 quân hậu
        res = max(res, current_sum)
        return

    for j in range(8):
        # Kiểm tra xem có thể đặt quân hậu tại (i-1, j) không
        if 0 <= j < 8 and 0 <= (i - j + 7) < 15 and 0 <= (i + j) < 15:
            if not cot[j] and not d1[i - j + 7] and not d2[i + j]:
                # Đặt quân hậu vào vị trí (i-1, j)
                cot[j] = True
                d1[i - j + 7] = True
                d2[i + j] = True
                current_sum += board[i - 1][j]  # Cộng điểm của ô (i-1, j)

                # Gọi đệ quy để đặt quân hậu tiếp theo
                Try(i + 1)

                # Quay lui: loại bỏ quân hậu và cập nhật lại tổng điểm
                cot[j] = False
                d1[i - j + 7] = False
                d2[i + j] = False
                current_sum -= board[i - 1][j]

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    # Khởi tạo bàn cờ và đọc giá trị
    ktao()
    
    # Khởi tạo các biến và mảng để đánh dấu
    cot = [False] * 8
    d1 = [False] * 15
    d2 = [False] * 15
    res = 0
    current_sum = 0

    # Thực hiện tìm kiếm tối ưu
    Try(1)

    # In ra kết quả cho mỗi bộ test
    print(res)
#end

#Bài 1. Tập hợp có tổng bằng S
#Begin
def Try(sum, cnt, pos):
    global ans
    # Nếu đã đủ k phần tử và tổng bằng s, tăng biến đếm
    if sum == s and cnt == k:
        ans += 1
        return

    # Thử các số từ pos đến n
    for j in range(pos, n + 1):
        if sum + j <= s and cnt + 1 <= k:
            Try(sum + j, cnt + 1, j + 1)

while True:
    # Đọc các giá trị n, k, s
    n, k, s = map(int, input().split())
    if n == 0 and k == 0 and s == 0:
        break

    ans = 0  # Biến đếm số lượng tập hợp thỏa mãn
    Try(0, 0, 1)
    print(ans) 
#End


#Bài 2. In dãy số
def Try(arr):
    # Độ dài hiện tại của dãy
    n = len(arr)
    if n == 0:
        return

    # In dãy hiện tại
    print("[", end="")
    for i in range(n):
        print(arr[i], end="")
        if i < n - 1:
            print(" ", end="")
    print("]")

    # Tạo dãy mới bằng cách cộng hai phần tử liên tiếp
    new_arr = [arr[i] + arr[i + 1] for i in range(n - 1)]

    # Gọi đệ quy cho dãy mới
    Try(new_arr)


# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    # Đọc số phần tử của dãy
    n = int(input())
    # Đọc dãy số
    arr = list(map(int, input().split()))

    # Gọi hàm đệ quy để in tam giác đặc biệt
    Try(arr)

#Bài 3 in dãy 2
#Begin
def Try(arr, result):
    # Độ dài hiện tại của dãy
    n = len(arr)
    if n == 0:
        return

    # Lưu dãy hiện tại vào danh sách kết quả
    result.append(arr)

    # Tạo dãy mới bằng cách cộng hai phần tử liên tiếp
    new_arr = [arr[i] + arr[i + 1] for i in range(n - 1)]

    # Gọi đệ quy cho dãy mới
    Try(new_arr, result)


# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    # Đọc số phần tử của dãy
    n = int(input())
    # Đọc dãy số
    arr = list(map(int, input().split()))

    # Khởi tạo danh sách để lưu các hàng của tam giác
    result = []
    Try(arr, result)

    # In kết quả từ dưới lên trên
    for row in reversed(result):
        print("[", end="")
        print(", ".join(map(str, row)), end="")
        print("]")
#End

#Begin
from itertools import permutations

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    # Đọc xâu ký tự
    s = input().strip()
    
    # Tạo tất cả các hoán vị của xâu s
    perm = sorted(set(permutations(s)))
    
    # In ra các hoán vị
    for p in perm:
        print("".join(p))
    print()  # Dòng trống giữa các bộ test
#end

#Bài 8. Di chuyển trong ma trận
#Begin
def inp():
    global M, N, matrix
    M, N = map(int, input().split())
    # Đọc ma trận
    matrix = []
    for _ in range(M):
        row = list(map(int, input().split()))
        matrix.append(row)

def Try(i, j):
    global ans
    # Nếu đã đến ô (M-1, N-1), tăng số đường đi
    if i == M - 1 and j == N - 1:
        ans += 1
        return
    
    # Di chuyển xuống dưới
    if i + 1 < N:
        Try(i + 1, j)
    
    # Di chuyển sang phải
    if j + 1 < M:
        Try(i, j + 1)

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    inp()  # Đọc ma trận
    ans = 0
    Try(0, 0)
    print(ans)

def inp():
    global n, m, matrix
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

def Try(i, j, current_sum):
    global ans
    # Nếu đến ô (n-1, m-1), cập nhật tổng lớn nhất
    if i == n - 1 and j == m - 1:
        ans = max(ans, current_sum)
        return

    # Di chuyển xuống dưới nếu có thể
    if i + 1 < n:
        Try(i + 1, j, current_sum + matrix[i + 1][j])
    
    # Di chuyển sang phải nếu có thể
    if j + 1 < m:
        Try(i, j + 1, current_sum + matrix[i][j + 1])

# Đọc dữ liệu đầu vào
inp()
ans = 0
Try(0, 0, matrix[0][0])

# In ra tổng lớn nhất
print(ans)

#End
def min_distance(x, y, visited):
    # Nếu đã đến một ô nước (W), trả về khoảng cách = 0
    if matrix[x][y] == 'W':
        return 0

    # Đặt giá trị ban đầu cho khoảng cách ngắn nhất là vô cực
    min_dist = float('inf')

    # Duyệt qua 4 hướng (lên, xuống, trái, phải)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        # Kiểm tra điều kiện biên và tránh ô đã thăm
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
            # Đánh dấu ô hiện tại là đã thăm
            visited[nx][ny] = True
            # Tìm khoảng cách từ ô lân cận đến nước
            dist = 1 + min_distance(nx, ny, visited)
            # Cập nhật khoảng cách nhỏ nhất
            min_dist = min(min_dist, dist)
            # Bỏ đánh dấu để thử các nhánh khác
            visited[nx][ny] = False

    return min_dist

# Đọc số lượng test case
T = int(input())
for _ in range(T):
    # Đọc kích thước ma trận
    M, N = map(int, input().split())

    # Đọc ma trận
    matrix = [input().strip() for _ in range(M)]

    # Tổng khoảng cách từ tất cả ô đất đến nước
    total_distance = 0

    # Tìm khoảng cách nhỏ nhất từ mỗi ô đất
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 'L':
                # Tạo mảng visited để tránh lặp lại các ô
                visited = [[False] * N for _ in range(M)]
                visited[i][j] = True
                # Tìm khoảng cách nhỏ nhất từ ô (i, j) đến nước
                total_distance += min_distance(i, j, visited)

    # In kết quả
    print(total_distance)

# cach 2
def find_min_distance(x, y, current_dist, visited):
    # Nếu đã đến một ô nước (W), trả về khoảng cách hiện tại
    if matrix[x][y] == 'W':
        return current_dist

    # Nếu khoảng cách hiện tại vượt quá giá trị nhỏ nhất đã biết, dừng nhánh này
    if current_dist >= memo[x][y]:
        return float('inf')

    # Cập nhật khoảng cách nhỏ nhất cho ô hiện tại
    memo[x][y] = current_dist

    # Tìm khoảng cách nhỏ nhất bằng cách thử tất cả các hướng
    min_dist = float('inf')
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            dist = find_min_distance(nx, ny, current_dist + 1, visited)
            min_dist = min(min_dist, dist)
            visited[nx][ny] = False

    return min_dist

# Đọc số lượng test case
T = int(input())
for _ in range(T):
    # Đọc kích thước ma trận
    M, N = map(int, input().split())

    # Đọc ma trận
    matrix = [input().strip() for _ in range(M)]

    # Tạo mảng memo để lưu khoảng cách nhỏ nhất
    memo = [[float('inf')] * N for _ in range(M)]

    # Tổng khoảng cách từ tất cả ô đất đến nước
    total_distance = 0

    # Tìm khoảng cách nhỏ nhất từ mỗi ô đất
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 'L':
                # Tạo mảng visited để tránh đi lại các ô đã thăm
                visited = [[False] * N for _ in range(M)]
                visited[i][j] = True
                # Tính khoảng cách nhỏ nhất từ ô (i, j) đến nước
                total_distance += find_min_distance(i, j, 0, visited)

    # In kết quả
    print(total_distance)
# Đề bài: Tìm tất cả các đường đi từ góc trên trái đến góc dưới phải trong một mê cung
# Cho một mê cung kích thước M x N, được biểu diễn dưới dạng ma trận nhị phân.

# Giá trị 1 đại diện cho ô có thể đi qua.
# Giá trị 0 đại diện cho ô bị chặn.
# Tìm tất cả các đường đi từ ô bắt đầu (0, 0) đến ô đích (M-1, N-1). Một đường đi hợp lệ chỉ được phép di chuyển qua các ô có giá trị 1 và theo các hướng:

# Sang phải.
# Xuống dưới.
# Nếu không có đường đi nào, trả về danh sách rỗng.
cach 1
def find_paths(x, y, path, visited):
    # Nếu đã đến đích, thêm đường đi vào danh sách
    if x == M - 1 and y == N - 1:
        results.append(path)
        return

    # Các hướng di chuyển: sang phải (R), xuống dưới (D)
    directions = [(0, 1, 'R'), (1, 0, 'D')]

    for dx, dy, move in directions:
        nx, ny = x + dx, y + dy

        # Kiểm tra điều kiện biên và tính hợp lệ
        if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            find_paths(nx, ny, path + move, visited)
            visited[nx][ny] = False  # Quay lui

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    # Đọc kích thước mê cung
    M, N = map(int, input().split())

    # Đọc mê cung
    maze = [list(map(int, input().split())) for _ in range(M)]

    # Khởi tạo danh sách kết quả và mảng visited
    results = []
    visited = [[False] * N for _ in range(M)]

    # Nếu ô bắt đầu hoặc ô kết thúc bị chặn, không có đường đi
    if maze[0][0] == 0 or maze[M-1][N-1] == 0:
        print("No Path")
    else:
        visited[0][0] = True
        find_paths(0, 0, "", visited)
        if results:
            for path in sorted(results):  # Sắp xếp kết quả theo thứ tự từ điển
                print(path)
        else:
            print("No Path")

cach 2
def find_paths(x, y, path, visited):
    # Nếu đã đến đích, thêm đường đi vào danh sách
    if x == M - 1 and y == N - 1:
        results.append(path)
        return

    # Các hướng di chuyển: sang phải (R), xuống dưới (D)
    directions = [(0, 1, 'R'), (1, 0, 'D')]

    for dx, dy, move in directions:
        nx, ny = x + dx, y + dy

        # Kiểm tra điều kiện biên và tính hợp lệ
        if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            find_paths(nx, ny, path + move, visited)
            visited[nx][ny] = False  # Quay lui

# Đọc số lượng test case
T = int(input())
output = []  # Danh sách lưu tất cả kết quả để ghi ra file

for _ in range(T):
    # Đọc kích thước mê cung
    M, N = map(int, input().split())

    # Đọc mê cung
    maze = [list(map(int, input().split())) for _ in range(M)]

    # Khởi tạo danh sách kết quả và mảng visited
    results = []
    visited = [[False] * N for _ in range(M)]

    # Nếu ô bắt đầu hoặc ô kết thúc bị chặn, không có đường đi
    if maze[0][0] == 0 or maze[M-1][N-1] == 0:
        output.append("No Path")
    else:
        visited[0][0] = True
        find_paths(0, 0, "", visited)
        if results:
            output.extend(sorted(results))  # Ghi các đường đi đã sắp xếp
        else:
            output.append("No Path")
    output.append("")  # Thêm dòng trống giữa các bộ test

# Ghi kết quả ra file
with open("output.txt", "w") as f:
    f.write("\n".join(output))


int n, m, ans = 0, a[105][105];
void inp(){
    cin >> n >> m;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            cin >> a[i][j];
        }
    }
} 


void Try(int i, int j, int sum){
    if(i == n && j == m){
        ans = max(ans, sum); 
        return;
        
    }
    if(i + 1 <= n){
        Try(i + 1, j, sum + a[i+1][j]);
    }
    if(j + 1 <= n){
        Try(i, j + 1, sum + a[i + 1][j]);
    }
}



int main(){
    int t;
    cin >> t;
    while(t--){
        inp();    
        ans = INT_MIN;
        Try(1, 1, a[1][1]);
        cout << ans << endl;    
    }
}


