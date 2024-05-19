import matplotlib.pyplot as plt
import math

def bubble_sort(mas):
    n = len(mas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mas[j] > mas[j+1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]
    return mas


# example
"""mas = [64, 34, 25, 12, 22, 11, 90]
print("Array: ", mas)
sorted_mas = bubble_sort(mas)
print("Sorted array:", sorted_mas)"""

arr1 = [n ** 2 for n in range(1, 20)]
arr2 = [n * math.log(n, 2) for n in range(1, 20)]

plt.figure(figsize=(10, 5))

plt.plot([n for n in range(1, 20)], arr1, marker='o', label='Bubble Sort')
plt.plot([n for n in range(1, 20)], arr2, marker='o', label='Method sort()')

plt.title('Comparison of Bubble Sort and Method sort() Number of Steps')
plt.xlabel('n')
plt.ylabel('number of steps')
plt.legend()

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True)) # making y-axis ticks as integer values

plt.savefig('graph1.png', format="png", dpi=300)
plt.clf()