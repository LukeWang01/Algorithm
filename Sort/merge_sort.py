
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp_li = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            tmp_li.append(li[i])
            i += 1
        else:
            tmp_li.append(li[j])
            i += 1

    while i <= mid:
        tmp_li.append(li[i])
        i += 1

    while j <= high:
        tmp_li.append(li[j])
        j += 1

    # high + 1, because the slice is [),
    li[low:high + 1] = tmp_li




def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


