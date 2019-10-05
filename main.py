from merge_sort import merge_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
import random
import time


def request_numbers():
    string = input("input a bunch of numbers delimited by a space ")
    string_array = string.split()
    num_list = []

    for entry in string_array:
        num_list.append(int(entry))

    return num_list


def random_or_not():
    ran = int(input("how many random numbers do you want in your list? (0 to make your own list) "))
    if ran == 0:
        return request_numbers()
    else:
        random_list = []
        for i in range(0, ran):
            random_list.append(random.randint(0, 100))
        return random_list


array = random_or_not()
ref_sorted_array = sorted(array)

merge_start = time.perf_counter_ns()
sorted_merge_list = merge_sort(array)
merge_end = time.perf_counter_ns()
if sorted_merge_list == ref_sorted_array:
    print("merge sort worked!")
    print("took " + str((merge_end - merge_start) / 1_000_000) + "ms")
else:
    print("merge sort failed!")

bubble_start = time.perf_counter_ns()
sorted_bubble_list = bubble_sort(array)
bubble_end = time.perf_counter_ns()
if sorted_bubble_list == ref_sorted_array:
    print("bubble sort worked!")
    print("took " + str((bubble_end - bubble_start) / 1000000) + "ms")
else:
    print("merge sort failed!")

insertion_start = time.perf_counter_ns()
sorted_insertion_list = insertion_sort(array)
insertion_end = time.perf_counter_ns()
if sorted_insertion_list == ref_sorted_array:
    print("insertion sort worked!")
    print("took " + str((insertion_end - insertion_start) / 1000000) + "ms")
else:
    print("merge sort failed!")
