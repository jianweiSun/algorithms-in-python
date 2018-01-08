
def binary_search(list_, item):
    first = 0
    last = len(list_) - 1
    found = False

    while first < last and not found:
        mid = (first + last) / 2
        mid_item = list_[mid]

        if mid_item == item:
            found = True
        elif mid_item > item:
            last = mid - 1
        else:  # mid_item < item
            first = mid + 1

    # first == last after looping
    return list_[first] == item


def recursive_binary_search(list_, item):

    if len(list_) == 1:
        return list_[0] == item
    else:
        mid = len(list_) / 2

        if list_[mid] == item:
            return True
        elif list_[mid] > item:
            return recursive_binary_search(list_[:mid], item)
        else:  # list_[mid] < item
            return recursive_binary_search(list_[mid+1:], item)


def recursive_binary_search_without_slice(list_, item, start_index=None, end_index=None):

    if not start_index and not end_index:
        start_index = 0
        end_index = len(list_) - 1

    if start_index == end_index:
        return list_[start_index] == item
    else:
        mid = (start_index + end_index) / 2

        if list_[mid] == item:
            return True
        elif list_[mid] > item:
            return recursive_binary_search_without_slice(list_, item, start_index, mid)
        else:  # list_[mid] < item
            return recursive_binary_search_without_slice(list_, item, mid+1, end_index)
