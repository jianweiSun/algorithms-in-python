
def bubble_sort(l):
    for pass_sum in range(len(l)-1, 0, -1):
        for i in range(pass_sum):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]


def bubble_sort_2(list_):
    pass_sum = len(list_) - 1
    while pass_sum > 0:
        for i in range(pass_sum):
            if list_[i] > list_[i+1]:
                list_[i], list_[i+1] = list_[i+1], list_[i]
        pass_sum -= 1


def short_bubble(l):
    for pass_sum in range(len(l)-1, 0, -1):
        is_exchange = True
        while is_exchange:
            is_exchange = False
            for i in range(pass_sum):
                if l[i] > l[i+1]:
                    is_exchange = True
                    l[i], l[i+1] = l[i+1], l[i]


def short_bubble_2(list_):
    pass_sum = len(list_) - 1
    is_exchange = True
    while pass_sum > 0 and is_exchange:
        is_exchange = False
        for i in range(pass_sum):
            if list_[i] > list_[i+1]:
                is_exchange = True
                list_[i], list_[i+1] = list_[i+1], list_[i]
        pass_sum -= 1
