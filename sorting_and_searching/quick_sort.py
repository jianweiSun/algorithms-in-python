
def quick_sort(list_, start, end):
    if end > start:
        split_position = partition(list_, start, end)
        quick_sort(list_, start, split_position-1)
        quick_sort(list_, split_position+1, end)


def partition(list_, start, end):
    pivot = list_[start]
    left_mark = start + 1
    right_mark = end

    done = False
    while not done:

        while left_mark <= right_mark and list_[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and list_[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            list_[left_mark], list_[right_mark] = list_[right_mark], list_[left_mark]

    list_[right_mark], list_[start] = list_[start], list_[right_mark]
    return right_mark
