def shell(arr, gap):
    counter = 0
    for i in range(gap, len(arr)):
        now = arr[i]
        j = i
        while j >= gap and arr[j - gap] > now:
            counter += 1
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = now
    return counter


def shell_sort(arr):
    counter = 0
    gap = len(arr) // 2
    while gap > 0:
        counter += shell(arr, gap)
        gap //= 2
    return counter
