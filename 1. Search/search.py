#
# https://www.bilibili.com/video/BV1uA411N7c5/?spm_id_from=333.788.recommend_more_video.0&vd_source=7b952f8a8ddeb2e3edf4bff8eae66f3f
#
# https://www.bilibili.com/video/BV1XL411g7qF?p=73&vd_source=7b952f8a8ddeb2e3edf4bff8eae66f3f
#
# Linear 1. Search
from Python.calculate_time import calculate_time


@calculate_time
def linear_search(ls, val):
    for i, v in enumerate(ls):
        if val == v:
            return i
    else:
        return None


# Binary 1. Search
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


