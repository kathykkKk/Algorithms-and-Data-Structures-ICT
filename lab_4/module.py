def quick_sort(arr):
    n = len(arr)
    if len(arr) <= 1:
        return arr
    else:
        element = arr[n // 2]
        less = [x for x in arr[:n // 2] + arr[n // 2 + 1:] if x <= element]
        greater = [x for x in arr[:n // 2] + arr[n // 2 + 1:] if x > element]
        return quick_sort(less) + [element] + quick_sort(greater)


def comb_sort(arr):
    n = len(arr)
    while True:
        n = int(n / 1.25)
        if n < 1:
            break
        i = 0
        while i + n < len(arr):
            if arr[i] > arr[i + n]:
                arr[i], arr[i + n] = arr[i + n], arr[i]
            i += 1
    return arr