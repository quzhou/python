"""https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated
by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(" ")
        size = len(l)
        if size != len(pattern):
            return False

        map1, map2 = {}, {}
        for i in range(size):
            if pattern[i] in map1:
                if map1[pattern[i]] != l[i]:
                    return False
            else:
                map1[pattern[i]] = l[i]

            if l[i] in map2:
                if map2[l[i]] != pattern[i]:
                    return False
            else:
                map2[l[i]] = pattern[i]

        return True

if __name__ == "__main__":
    print Solution().wordPattern("abba", "dog dog dog dog")