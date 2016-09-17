"""https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :param nums:
        :param target:
        :return: index
        """
        size = len(nums)
        if size == 0:
            return -1
        low, high = 0, size - 1
        while low < high:
            mid = low + (high - low) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # low == high
        if target == nums[low]:
            return low
        elif target < nums[low]:
            return low
        else:
            return low + 1



