def swap(array, pos):
    temp = array[pos]
    array[pos] = array[pos - 1]
    array[pos - 1] = temp


def insertion_sort(array):
    array_size = len(array)
    for i in range(1, array_size):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j)
            j = j - 1
    return array
