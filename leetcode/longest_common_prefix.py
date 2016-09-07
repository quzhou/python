"""https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :param strs: list of string
        :return: str
        """
        ret = ""
        if len(strs) == 0:
            return ret

        stra = strs[0]
        for i in range(len(stra)):
            match = True
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != stra[i]:
                    match = False
                    break
            if match:
                ret += stra[i]
            else:
                break

        return ret

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["aca", "cba"])
