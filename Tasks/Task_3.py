import random
import timeit
from tabulate import tabulate

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_data(size, case="random"):
    if case == "sorted":
        return list(range(size))
    elif case == "reversed":
        return list(range(size, 0, -1))
    else:
        return [random.randint(0, size) for _ in range(size)]

def compare_algorithms():
    sizes = [1000, 3000, 6000]
    cases = ["random", "sorted", "reversed"]
    table = []

    for size in sizes:
        for case in cases:
            data = generate_data(size, case)

            t_insert = timeit.timeit(lambda: insertion_sort(data), number=1)
            t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
            t_timsort = timeit.timeit(lambda: sorted(data), number=1)

            table.append([
                size,
                case,
                f"{t_insert:.4f} с",
                f"{t_merge:.4f} с",
                f"{t_timsort:.4f} с"
            ])

    headers = ["Розмір", "Тип даних", "Insertion Sort", "Merge Sort", "Timsort (sorted)"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    compare_algorithms()