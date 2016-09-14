#TODO: NlogN

"""https://leetcode.com/problems/longest-increasing-subsequence/
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example, Given [10, 9, 2, 5, 3, 7, 101, 18], the longest increasing subsequence is
[2, 3, 7, 101], therefore the length is 4.

Note that there may be more than one LIS combination, it is only necessary for you to
return the length.

Your algorithm should run in O(n2) complexity. Could you improve it to O(n log n)
time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        max = 1
        length = [1]  # length of LIS ending at
        for i in range(1, size):
            maxLen, curLen = 0, 0
            for k in range(i):
                if nums[k] < nums[i]:
                    curLen = length[k] + 1
                else:
                    curLen = 1

                if curLen > maxLen:
                    maxLen = curLen

            length.append(maxLen)
            if length[i] > max:
                max = length[i]

        return max

if __name__ == "__main__":
    print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

