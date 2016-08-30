"""https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
"""

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [min(i, map[target - nums[i]]), max(i, map[target - nums[i]])]
            else:
                map[nums[i]] = i
        return [-1, -1]


    def twoSum1(self, nums, target):
        length = len(nums)
        if length < 2:
            return [-1, -1]
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]


    # this is wrong as sorting changes index
    def twoSum2(self, nums, target):
        """
        :param nums: array of integer
        :param target:
        :return: index like [0, 3]
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]


if __name__ == "__main__":
    print Solution().twoSum([3, 2, 4], 6)