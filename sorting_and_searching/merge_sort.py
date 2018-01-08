def merge(a, b):
    result = list()
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:] or b[j:]
    return result


def merge_sort(list_):
    if len(list_) <= 1:
        return list_
    else:
        mid = len(list_)/2
        left = merge_sort(list_[:mid])
        right = merge_sort(list_[mid:])
        return merge(left, right)


def merge_sort_by_index(list_, start, end):
    if end - start <= 1:
        return list_[start:end]
    else:
        mid = (start + end) / 2
        left = merge_sort_by_index(list_, start, mid)
        right = merge_sort_by_index(list_, mid, end)
        return merge(left, right)


def merge_sort_2(alist):
    print("Splitting ", alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort_2(lefthalf)
        merge_sort_2(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)
