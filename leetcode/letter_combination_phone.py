"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a digit string, return all possible letter combinations that the number could represent.
Input "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        result = []
        self.helper(digits, result)
        return result

    def helper(self, digits, result):
        map = {
            '0': ['+'],
            '1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        size = len(digits)
        if size == 1:
            for elem in map[digits[0]]:
                result.append(elem)
            return

        strList = []
        self.helper(digits[1:], strList)
        for first in map[digits[0]]:
            for right in strList:
                result.append(first + right)

if __name__ == "__main__":
    print Solution().letterCombinations('22')

