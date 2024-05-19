import module
import timeit
import random


"""arr = input("Введите массив: ").split(' ')
case = int(input("Выберите сортировку (1 - быстрая, 2 - расческой): "))

print(f"Быстрая сортировка массива {arr}: {module.quick_sort(arr)}" if case == 1 else
      f"Cортировка расческой массива {arr}: {module.comb_sort(arr)}")"""


arr = [random.randint(0, 100) for i in range(500)] + [i for i in range(700)] + [random.randint(0, 300) for i in range(300)] + [i for i in range(500)]
print(arr)

time_quick_sort = timeit.timeit('module.quick_sort(arr)', globals=globals(), number=1000)
print("\nВремя выполнения quick_sort:", time_quick_sort)

# Измерение времени работы comb_sort
time_comb_sort = timeit.timeit('module.comb_sort(arr)', globals=globals(), number=1000)
print("\nВремя выполнения comb_sort:", time_comb_sort)
