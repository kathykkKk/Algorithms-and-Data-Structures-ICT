def steals(K, weights, values):
    n = len(weights)
    c = [[0 for _ in range(K + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, K + 1):
            if weights[i - 1] <= j:
                c[i][j] = max(c[i - 1][j], c[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                c[i][j] = c[i - 1][j]
    result = c[n][K]

    stolen_items = []
    w = K
    for i in range(n, 0, -1):
        if c[i][w] != c[i - 1][w]:
            stolen_items.append(i - 1)
            w -= weights[i - 1]

    return result, stolen_items


def max_steal_dynamic(M, K, exhibits):
    total_value = 0
    weights = [item[0] for item in exhibits]
    values = [item[1] for item in exhibits]
    for i in range(M):
        x = steals(K, weights, values)
        total_value += x[0]
        stolen = x[1]
        stolen.sort(reverse=True)
        for j in stolen:
            del weights[j]
            del values[j]
    return total_value


# пример 1
M = 3
K = 4
exhibits = [(2, 1500), (1, 1000), (4, 5000), (3, 2000), (2, 1250), (3, 2500)]
print(max_steal_dynamic(M, K, exhibits))

# пример 2
M = 2
K = 4
exhibits = [(2, 1500), (1, 1000), (3, 3000), (4, 2000)]
print(max_steal_dynamic(M, K, exhibits))

