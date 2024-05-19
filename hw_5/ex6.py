def exponential_filter(data, alpha):
    result = [data[0]]
    for i in range(1, len(data)):
        result.append(result[i - 1] + alpha * (data[i] - result[i - 1]))
    return result


data = [10, 20, 30, 40, 50]
print("Изначальный ряд: ", end='')
for i in data:
    print(i, end=' ')
print()
alpha = 0.2
smoothed_data = exponential_filter(data, alpha)
print("Ряд после экспоненциального сглаживания: ", end='')
for i in smoothed_data:
    print(i, end=' ')

