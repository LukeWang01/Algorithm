# 1. Two Sum
#
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


# O(nlogn)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x:x[0])
        l = len(new_nums)
        for i in range(l):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                res = self.binary_search(new_nums, i + 1, l - 1, b)
            else:
                res = self.binary_search(new_nums, 0, i - 1, b)

            if res is not None:
                return [new_nums[i][1], new_nums[res][1]]

    def binary_search(self, lst, left, right, val):
        while left <= right:
            mid = (left + right) // 2

            if lst[mid][0] == val:
                return mid
            elif lst[mid][0] < val:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return None


# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l):
            a = numbers[i]
            b = target - a
            if b >= a:
                res = self.binary_search(numbers, i + 1, l - 1, b)
            else:
                res = self.binary_search(numbers, 0, i - 1, b)

            if res is not None:
                return [i + 1, res + 1]

    def binary_search(self, lst, left, right, val):
        while left <= right:
            mid = (left + right) // 2

            if lst[mid] == val:
                return mid
            elif lst[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return None

#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        start, end = 0, len(numbers) -1
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start + 1, end + 1]
            if s < target:
                start += 1
            else:
                end -= 1