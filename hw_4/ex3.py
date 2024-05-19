def max_increasing_sequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


# Пример использования функции
arr = [-3, -2, 1, 5, 4, 3, 6]
print(f"Максимальная длина возрастающей подпоследовательности\nдля массива {arr} равна {max_increasing_sequence(arr)}")
