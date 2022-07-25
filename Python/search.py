# Linear Search
from Python.calculate_time import calculate_time


@calculate_time
def linear_search(ls, val):
    for i, v in enumerate(ls):
        if val == v:
            return i
    else:
        return None


# Binary Search
@calculate_time
def binary_search(sorted_li, val):
    left = 0
    right = len(sorted_li) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_li[mid] == val:
            return mid
        elif sorted_li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1

    else:
        return None


