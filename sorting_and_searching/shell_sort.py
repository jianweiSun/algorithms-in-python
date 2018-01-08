def shell_sort(list_):
    gap_size = len(list_) / 2

    while gap_size > 0:
        for start_position in range(gap_size):
            gap_insertion_sort(list_, start_position, gap_size)

        print "After insertion sort of gap_size:{}, the list is {}.".format(gap_size, list_)

        gap_size = gap_size / 2


def gap_insertion_sort(list_, start_position, gap_size):

    for i in range(start_position+gap_size, len(list_), gap_size):
        current_value = list_[i]
        position = i

        while position > start_position and list_[position-gap_size] > current_value:
            list_[position] = list_[position-gap_size]
            position -= gap_size

        list_[position] = current_value
