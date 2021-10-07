def put(arr, idx):
    counter = 0
    for i in range(idx - 1, -1, -1):
        if arr[i + 1] < arr[i]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            counter += 1
    return counter


def insertion_sort(arr):
    counter = 0
    for i in range(len(arr)):
        counter += put(arr, i)
    return counter
