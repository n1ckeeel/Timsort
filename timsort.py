import random
import time


MIN_RUN = 32


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def timsort(arr):
    n = len(arr)
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2


def timed_timsort(n):
    arr = [random.randint(0, 10_000) for _ in range(n)]
    unsorted_copy = arr.copy()

    start = time.perf_counter()
    timsort(arr)
    end = time.perf_counter()

    return unsorted_copy, arr, end - start


if __name__ == "__main__":
    n = 10
    unsorted_list, sorted_list, t = timed_timsort(n)

    print("Unsorted:", unsorted_list)
    print("Sorted:", sorted_list)
    print(f"Run time: {t:.6f} seconds")
