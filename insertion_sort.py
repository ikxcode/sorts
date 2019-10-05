def swap(array, pos):
    temp = array[pos]
    array[pos] = array[pos - 1]
    array[pos - 1] = temp


def insertion_sort(array):
    steps = 0
    array_size = len(array)
    for i in range(1, array_size):
        j = i
        old_steps = steps
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j)
            j = j - 1
            steps = steps + 1
        if steps == old_steps:
            steps = steps + 1
    print("Steps: " + str(steps))
    return array
