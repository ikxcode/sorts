
def find_letter(name_letter):
    index = 0
    for letter in alphabet:
        if name_letter == letter:
            return index
        index += 1


def bubble_sort_alphabetical(name_list):
    list_size = len(name_list)

    for not_i in range(list_size):
        for i in range(list_size - 1):
            name_1 = name_list[i]
            name_2 = name_list[i + 1]
            compared = False
            letter_position = 0
            while not compared:
                name_letter_1 = name_1[letter_position].upper()
                name_letter_2 = name_2[letter_position].upper()
                name_index_1 = find_letter(name_letter_1)
                name_index_2 = find_letter(name_letter_2)
                if name_index_1 > name_index_2:
                    temp = name_list[i + 1]
                    name_list[i + 1] = name_list[i]
                    name_list[i] = temp
                    compared = True
                elif name_index_1 < name_index_2:
                    compared = True
                letter_position += 1
        print(name_list)


    return name_list


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

name_list_boys = ["Oliver", "George", "Harry", "Noah", "Jack",
                  "Leo", "Arthur", "Muhammad", "Oscar", "Charlie"]

name_list_girls = ["Olivia", "Amelia", "Ava", "Isla", "Emily",
                   "Mia", "Isabella", "Sophia", "Ella", "Grace"]

name_list_test = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n",
                  "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]

print(bubble_sort_alphabetical(name_list_boys))
