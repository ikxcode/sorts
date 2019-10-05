from merge_sort import merge_sort
from bubble_sort import bubble_sort


def request_numbers():
    string = input("input a bunch of numbers delimited by a space ")
    string_array = string.split()
    array = []

    for entry in string_array:
        array.append(int(entry))

    return array

# sorted_list = merge_sort(array, 0, "root")


array = request_numbers()
sorted_list = bubble_sort(array)

print(sorted_list)
