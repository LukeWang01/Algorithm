
def sift(li, low, high):
    """
    sift the root with child
    :param li: list
    :param low: index, heap top, root node
    :param high: index, heap bottom, last element of heap
    :return:
    """
    i = low  # root node
    j = 2 * i + 1  # left children
    tmp = li[low]  #
    while j <= high:
        if j + 1 <= high and li[j+1] > li[j]:  # right > left
            j = j + 1  # switch to the greater one
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i in range((n -2)//2, -1, -1):
        sift(li, i, n-1)  # build the heap, let the last element always be the "high"

    for i in range(n-1, -1, -1):  # i is the last element of the heap
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i - 1 is the new high index


import heapq
import random

li = list(range(100))
random.shuffle(li)

heapq.heapify(li)

heapq.heappop(li)


