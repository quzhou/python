"""https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 2:
            return 0
        i = 0
        j = length - 1
        max = 0
        while i < j:
            size = (j - i) * min(height[i], height[j])
            if size > max:
                max = size

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max

