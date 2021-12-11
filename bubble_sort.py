def bubble_sort(source_list):
    array = source_list.copy()
    list_size = len(array)
    swaps = 0

    for i in range(list_size - 1):
        for j in range(list_size - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 1

    print(str(swaps) + " swaps")

    return array
