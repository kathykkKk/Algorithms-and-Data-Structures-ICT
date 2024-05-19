def min_operations(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            dp[i][j] = float('infinity')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i][0] * arr[k][1] * arr[j][1])

    return dp[0][n - 1]


# пример
matrices = [(3, 3), (3, 6), (6, 1), (1, 5), (5, 12)]
result = min_operations(matrices)
print(f"Для набора матриц {matrices} минимальное число операций равно {result}")
