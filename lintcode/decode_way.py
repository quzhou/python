"""http://www.lintcode.com/en/problem/decode-ways/
A message containing letters from A-Z is being encoded to numbers
using the following mapping:
'A' -> 1
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.
For example, the number of ways decoding 12 is 2.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :param s: e.g. "192611"
        :return: int
        """
        size = len(s)
        if size == 0 or (size == 1 and s[0] == '0'):
            return 0
        nums = [1]  # number of decodings ending at i
        for i in range(1, size):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                if i >= 2:
                    nums.append(nums[i - 2])
                else:
                    nums.append(1)
            elif s[i] == '7' or s[i] == '8' or s[i] == '9':
                if s[i - 1] == '1':
                    if i >= 2:
                        nums.append(nums[i - 1] + nums[i - 2])
                    else:
                        nums.append(2)
                else:
                    nums.append(nums[i-1])
            else:
                if s[i-1] == '1' or s[i-1] == '2':
                    if i >= 2:
                        nums.append(nums[i - 1] + nums[i - 2])
                    else:
                        nums.append(2)
                else:
                    nums.append(nums[i - 1])

        return nums[size-1]

if __name__ == "__main__":
    print Solution().numDecodings("192611") # "19261001" -> 0

