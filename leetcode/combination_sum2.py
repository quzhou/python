"""https://leetcode.com/problems/combination-sum-ii/
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

For example, [10, 1, 2, 7, 6, 1, 5], target is 8:
The solution set is:
[
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :param candidates: list[int]
        :param target: int
        :return: list[list[int]]
        """
        if len(candidates) == 0:
            return []
        output = []
        self.helper(candidates, target, output)

        for elem in output:
            elem.sort()

        result = []
        for elem in output:
            if elem not in result:
                result.append(elem)
        return result

    def helper(self, candidates, target, result):
        size = len(candidates)
        if size == 1:
            if target == 0:
                result.append([])
                return

            if candidates[0] == target:
                x = [candidates[0]]
                result.append(x)
                return
            else:
                return

        i = 0
        remain = target - candidates[0] * i
        while remain >= 0 and i < 2:
            lista = [candidates[0]] * i
            listlistb = []
            self.helper(candidates[1:], remain, listlistb)
            for right in listlistb:
                newlist = lista + right
                result.append(newlist)
            i += 1
            remain = target - candidates[0] * i


if __name__ == "__main__":
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)