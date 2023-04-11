def sample(A, n):
    if n == 1:
        return 1
    sum = 0
    for i in range(n):
        sum += A[i]
    tmp = sum + sample(A, n//3)
    return tmp

# 입력 예시
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(A)
result = sample(A, n)

print(result)