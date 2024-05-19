import matplotlib.pyplot as plt
import math

arr = [n for n in range(1, 20)]
arr1 = [1 for n in arr]
arr2 = [int(math.log(n, 2)) + 1 if math.log(n, 2) % 1 != 0 else int(math.log(n, 2)) for n in arr]
arr3 = [n ** 2 for n in arr]
arr4 = [2 ** n for n in arr]

for i in range(16):
    print(i, arr1[i], '\t', arr2[i], '\t', arr3[i], '\t', arr4[i], '\t')

plt.figure(figsize=(10, 10))

plt.plot(arr, arr1, marker='o', label='O(1)')
plt.plot(arr, arr2, marker='o', label='O(logn)')
plt.plot(arr, arr3, marker='o', label='O(n^2)')
plt.plot(arr, arr4, marker='o', label='O(2^n)')

plt.title('Comparison of Number of Steps for Different Complexity')
plt.xlabel('n')
plt.ylabel('number of steps')
plt.legend()

plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

#plt.savefig('graph2.png', format="png", dpi=300)
#plt.show()