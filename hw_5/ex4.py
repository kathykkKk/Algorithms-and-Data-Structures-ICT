def count_ways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


n = int(input("Введите количество ступенек: "))
print(f"Количество способов перемещения по лестнице из {n} ступенек: {count_ways(n)}")