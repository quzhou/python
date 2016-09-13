"""https://leetcode.com/problems/longest-palindromic-substring/
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""

class Solution(object):
    # O(n) How to construct suffix array in linear time?
    def longestPalindrome(self, s):
        size = len(s)
        max = 0
        left = right = -1
        dict = [[False for i in range(size)] for i in range(size)]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dict[i][j] = (s[i] == s[j]) and (j - i < 2 or dict[i+1][j-1])
                if dict[i][j]:
                    if j - i + 1 > max:
                        max = j - i + 1
                        left = i
                        right = j

        return s[left:right+1]


    # O(n^2)
    def longestPalindrome3(self, s):
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
    print Solution().longestPalindrome("geeksskeeg")
