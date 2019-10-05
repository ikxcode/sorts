from merge_sort import merge_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort


def request_numbers():
    string = input("input a bunch of numbers delimited by a space ")
    string_array = string.split()
    array = []

    for entry in string_array:
        array.append(int(entry))

    return array


array = request_numbers()
sorted_merge_list = merge_sort(array)
sorted_bubble_list = bubble_sort(array)
sorted_insertion_list = insertion_sort(array)

print("This list was sorted by the merge sort: " + str(sorted_merge_list))
print("This list was sorted by the bubble sort: " + str(sorted_bubble_list))
print("This list was sorted by the insertion sort: " + str(sorted_insertion_list))
