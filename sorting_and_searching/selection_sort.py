
def selection_sort(list_):
    for pass_total in range(len(list_), 1, -1):
        max_index = 0
        for i in range(pass_total):
            if list_[i] > list_[max_index]:
                max_index = i
        list_[pass_total-1], list_[max_index] = list_[max_index], list_[pass_total-1]


def selection_sort_2(list_):
    pass_total = len(list_)
    while pass_total > 1:
        max_index = 0
        for i in range(pass_total):
            if list_[i] > list_[max_index]:
                max_index = i
        list_[pass_total - 1], list_[max_index] = list_[max_index], list_[pass_total - 1]
        pass_total -= 1
