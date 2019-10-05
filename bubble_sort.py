def bubble_sort(sourceList):
    array = sourceList.copy()
    list_size = len(array)

    for not_i in range(list_size):
        for i in range(list_size - 1):
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp

    return array
