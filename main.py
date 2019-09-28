from merge_sort import merge_sort
# array = [2,99,1,32,3,7,4,34,5,43,5,53]
# array = [2,3,2]

def request_numbers():
    string = input("input a bunch of numbers delimited by a space ")
    string_array = string.split()
    array = []

    for entry in string_array:
        array.append(int(entry))

    return array

# sorted_list = merge_sort(array, 0, "root")


array = request_numbers()
sorted_list = merge_sort(array)

print(sorted_list)
