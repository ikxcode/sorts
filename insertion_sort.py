def swap(array, pos, swaps):
    array[pos], array[pos - 1] = array[pos - 1], array[pos]
    swaps += 1

    return swaps


def insertion_sort(array):
    swaps = 0
    array_size = len(array)
    for i in range(1, array_size):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swaps = swap(array, j, swaps)
            j = j - 1
    print(str(swaps) + " swaps")

    return array
