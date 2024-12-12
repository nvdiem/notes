

# Sử dụng hàm
if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = input().strip()
        matrix.append(row)
        
    print(matrix)