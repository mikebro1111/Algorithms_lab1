def find(arr, idx, counter):
    min_index = idx
    min_value = arr[idx]
    for i in range(idx + 1, len(arr)):
        counter += 1
        if min_value > arr[i]:
            min_value = arr[i]
            min_index = i
    return min_index, counter


def selection_sort(arr):
    counter = 0
    for i in range(len(arr)):
        idx, counter = find(arr, i, counter)
        arr[idx], arr[i] = arr[i], arr[idx]
    return counter
