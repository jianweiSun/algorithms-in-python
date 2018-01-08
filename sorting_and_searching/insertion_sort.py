
def insertion_sort(list_):
    for i in range(1, len(list_)):
        current_value = list_[i]
        position = i
        while position > 0 and list_[position-1] > current_value:
            list_[position] = list_[position-1]
            position -= 1

        list_[position] = current_value


def insertion_sort_2(list_):
    for i in range(1, len(list_)):
        current_value = list_[i]
        for j in range(i, 0, -1):
            if list_[j-1] > current_value:
                list_[j] = list_[j-1]
                if j == 1:
                    list_[0] = current_value
            else:
                list_[j] = current_value
                break
