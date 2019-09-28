def merge_sort(array):
    array_size = len(array)
    if array_size == 1:
        return array

    # Split the Array
    array_middle = round(array_size / 2)
    array1 = array[0:array_middle]
    array2 = array[array_middle: array_size]

    # Recurse with each split Array
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)

    return sort_and_merge(array1, array2)


def sort_and_merge(array1, array2):
    merged_array = []

    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            smallest_num = array1.pop(0)
            merged_array.append(smallest_num)
        else:
            smallest_num = array2.pop(0)
            merged_array.append(smallest_num)

    if len(array1) > 0:
        merged_array.extend(array1)
    else:
        merged_array.extend(array2)

    return merged_array
