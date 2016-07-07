""" https://leetcode.com/problems/string-to-integer-atoi/
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below
and ask yourself what are the possible input cases.
"""

class Solution(object):
    def my_atoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        sign = 1
        ret = 0
        i = 0
        if str[0] == '+':
            i += 1
        elif str[0] == '-':
            sign = -1
            i += 1
        """
        if not str.isdigit():
            raise ValueError("Input string must be digits.")
        """
        # python way
        # int(new_str)

        for i in range(i, len(str)):
            if str[i] < '0' or str[i] > '9':
                break
            else:
                ret = ret * 10 + int(str[i])
        ret *= sign
        MaxInt = (1 << 31) - 1
        if ret >= MaxInt:
            return MaxInt
        elif ret < -MaxInt:
            return -MaxInt - 1
        return ret

def main():
    x = Solution()
    print x.my_atoi("   -2345 ")

if __name__ == "__main__":
    main()
