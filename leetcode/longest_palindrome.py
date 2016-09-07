"""https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen, maxStr = 0, ""
        for i in range(len(s)):
            str = self.longestSubPalin(i, s)
            if len(str) > maxLen:
                maxLen = len(str)
                maxStr = str

        return maxStr

    def longestSubPalin(self, index, s):
        i, j = index - 1, index + 1
        start = end = index
        while i >= 0 and j < len(s) and s[i] == s[j]:
            start = i
            end = j
            i -= 1
            j += 1
        str = s[start:end+1]

        i, j = index, index + 1
        start = end = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            start = i
            end = j
            i -= 1
            j += 1
        if end - start > 0:
            str2 = s[start:end+1]
            if len(str) > len(str2):
                return str
            else:
                return str2
        else:
            return str

if __name__ == "__main__":
    print Solution().longestPalindrome("bb")



