"""https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element. The majority element is the element
that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :param nums: list[int]
        :return: int
        """
        idx, count, size = -1, 0, len(nums)
        for i in range(size):
            if count == 0:
                idx = i
                count = 1
            else:
                if nums[i] == nums[idx]:
                    count += 1
                else:
                    count -= 1

        count = 0
        for i in range(size):
            if nums[i] == nums[idx]:
                count += 1
        if count > (size / 2):
            return nums[idx]
        else:
            return None

if __name__ == "__main__":
    arr = [3, 2, 3, 17, 3, 4, 3, 9, 3]
    print Solution().majorityElement(arr)