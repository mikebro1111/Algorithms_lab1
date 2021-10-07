def combine(arr, left, mid, right):
    counter = 0
    idx1 = 0
    idx2 = 0
    arr_left = arr[left:mid + 1]
    arr_right = arr[mid + 1:right + 1]
    now = left
    while idx1 < len(arr_left) and idx2 < len(arr_right):
        counter += 1
        if arr_left[idx1] < arr_right[idx2]:
            arr[now] = arr_left[idx1]
            idx1 += 1
        else:
            arr[now] = arr_right[idx2]
            idx2 += 1
        now += 1
    while idx1 < len(arr_left):
        arr[now] = arr_left[idx1]
        now += 1
        idx1 += 1
    while idx2 < len(arr_right):
        arr[now] = arr_right[idx2]
        now += 1
        idx2 += 1
    return counter


def _merge_sort(arr, left, right):
    counter = 0
    if left == right:
        return
    mid = (left + right) // 2
    _merge_sort(arr, left, mid)
    _merge_sort(arr, mid + 1, right)

    counter += combine(arr, left, mid, right)
    return counter


def merge_sort(arr):
    return _merge_sort(arr, 0, len(arr) - 1)
