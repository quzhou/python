"""https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLen, endLen, startIdx = 0, 0, 0
        last = {}  # last index that number has appeared
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= startIdx:
                startIdx = last[s[i]] + 1
            last[s[i]] = i

            endLen = i - startIdx + 1
            if endLen > maxLen:
                maxLen = endLen

        return maxLen

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abba")
