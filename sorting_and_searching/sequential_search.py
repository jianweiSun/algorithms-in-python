
def sequential_search(list_, item):

    pos = 0
    is_found = False

    while pos < len(list_) and not is_found:
        if list_[pos] == item:
            is_found = True
        else:
            pos += 1

    return is_found, pos


def ordered_sequential_search(list_, item):
    for i in range(len(list_)):
        if list_[i] == item:
            return True, i
        elif list_[i] > item:
            return False
    return False

