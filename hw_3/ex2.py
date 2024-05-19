def max_steal(M, K, exhibits):
    may_be_stolen = [i for i in exhibits if i[0] <= K]
    may_be_stolen.sort(key=lambda x: (x[1] / x[0], x[1]), reverse=True)
    total_value = 0
    num_of_exhibits = len(may_be_stolen)
    cnt = 0
    stolen = []
    for i in range(M):
        total_weight = 0
        for j in range(num_of_exhibits):
            if j not in stolen:
                if total_weight + may_be_stolen[j][0] <= K:
                    total_weight += may_be_stolen[j][0]
                    total_value += may_be_stolen[j][1]
                    stolen.append(j)
                    cnt += 1
    return total_value


# пример 1
M = 3
K = 4
exhibits = [(2, 1500), (1, 1000), (4, 5000), (3, 2000), (2, 1250), (3, 2500)]
print(max_steal(M, K, exhibits))

# пример 2 - неоптимальный вывод
M = 2
K = 4
exhibits = [(2, 1500), (1, 1000), (3, 3000), (4, 2000)]
print(max_steal(M, K, exhibits))



