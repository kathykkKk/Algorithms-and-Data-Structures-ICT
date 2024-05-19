def find_change(N, M1, S1, M2, S2, M3, S3, M4, S4):
    coins = [S1, S2, S3, S4]
    counts = [M1, M2, M3, M4]
    for i in range(3):
        for j in range(0, 3 - i):
            if coins[j] > coins[j + 1]:
                coins[j], coins[j + 1] = coins[j + 1], coins[j]
                counts[j], counts[j + 1] = counts[j + 1], counts[j]
    change = N
    result = {}
    for i in range(3, -1, -1):
        while change >= coins[i] and counts[i] > 0:
            change -= coins[i]
            counts[i] -= 1
            if coins[i] in result:
                result[coins[i]] += 1
            else:
                result[coins[i]] = 1
    if change == 0:
        return result
    else:
        return "Невозможно дать сдачу"


# Пример использования
N = 28
M1, S1 = 2, 10
M2, S2 = 5, 5
M3, S3 = 3, 2
M4, S4 = 7, 1

res = find_change(N, M1, S1, M2, S2, M3, S3, M4, S4)
for i in res:
    print(f"Монет номинала {i}: {res[i]}")
