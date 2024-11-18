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
