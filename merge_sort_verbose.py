def merge_sort(array, recursion, caller_label):
    recursion = recursion + 1
    print("\n### Starting Recursion: " + str(recursion) + " for  " + caller_label)

    array_size = len(array)
    if array_size == 1:
        print("Recursion " + str(recursion) + " returning " + str(array) + ". Single entry.\n")
        return array

    array_middle = round(array_size / 2)
    array1 = array[0:array_middle]
    array2 = array[array_middle: array_size]

    label_a1 = "A1_" + str(recursion)
    label_a2 = "A2_" + str(recursion)
    print("Recursion US " + str(recursion) + ", " + label_a1 + ": " + str(array1))
    print("Recursion US " + str(recursion) + ", " + label_a2 + ": " + str(array2))

    array1 = merge_sort(array1, recursion, label_a1)
    array2 = merge_sort(array2, recursion, label_a2)

    print("### Continuing Recursion: " + str(recursion) + " for  " + caller_label)

    print("Recursion SD " + str(recursion) + ", " + label_a1 + ": " + str(array1))
    print("Recursion SD " + str(recursion) + ", " + label_a2 + ": " + str(array2))

    print("Returning Recursion " + str(recursion) + " for caller " + caller_label + "." + str(array1) + ", " + str(
        array2))

    return merge(array1, array2)


def merge(array1, array2):
    merged_array = []

    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            smallest_num = array1.pop(0)
            merged_array.append(smallest_num)
        else:
            smallest_num = array2.pop(0)
            merged_array.append(smallest_num)

    while len(array1) > 0:
        smallest_num = array1.pop(0)
        merged_array.append(smallest_num)

    while len(array2) > 0:
        smallest_num = array2.pop(0)
        merged_array.append(smallest_num)

    return merged_array

