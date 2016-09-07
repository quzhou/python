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


def wordPattern(self, pattern, str):
    pat = {}
    for i in range(len(pattern)):
        idx = []
        if pattern[i] in pat:
            idx = pat[pattern[i]]
        idx.append(i)
        pat[pattern[i]] = idx

    map = {}
    strs = str.split(" ")
    for i in range(len(strs)):
        index = []
        if strs[i] in map:
            index = map[strs[i]]
        index.append(i)
        map[strs[i]] = index

    if len(pat) != len(map):
        return False

    for