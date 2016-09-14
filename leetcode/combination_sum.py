"""https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

For example, [2, 3, 6, 7], target is 7:
The solution set is:
[
    [7],
    [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
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
        # print "========"
        # print "candidates: "
        # print candidates
        # print "target: "
        # print target
        size = len(candidates)
        if size == 1:
            if target % candidates[0] == 0:
                x = [candidates[0]] * (target / candidates[0])
                result.append(x)
                return
            else:
                return

        i = 0
        remain = target - candidates[0] * i
        while remain >= 0:
            lista = [candidates[0]] * i
            listlistb = []
            self.helper(candidates[1:], remain, listlistb)

            # print "********"
            # print "listlistb for"
            # print remain
            # print listlistb
            # print "********"

            for right in listlistb:
                newlist = lista + right
                result.append(newlist)

            i += 1
            remain = target - candidates[0] * i


if __name__ == "__main__":
    print Solution().combinationSum([2, 3, 2, 7], 5)