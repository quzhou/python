"""https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

C(0) = 1, C(1) = 1, C(2) = 2. n = 3, the result is:
[
    "((()))"
    "(()())"
    "(())()"
    "()(())"
    "()()()"
]
"""

# Catalan number (A)B
# C(i+1) = sigma(0, i) C(k)C(i-k)

class Solution(object):
    def generateParentheses(self, n):
        results = [[""], ["()"]]
        for i in range(2, n+1):
            res_i = []
            for k in range(0, i):
                for left in results[k]:
                    for right in results[i-1-k]:
                        res_i.append("(" + left + ")" + right)
            results.append(res_i)

        return results[n]

if __name__ == "__main__":
    results = Solution().generateParentheses(3)
    print results


