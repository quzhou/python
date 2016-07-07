"""https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""

class Solution(object):
    def get_sum(self, a, b):
        """
        :param a:
        :param b:
        :return: int
        """
        while b != 0:
            c = a & b
            a = a ^ b
            b = c << 1

        return a

def main():
    x = Solution()
    print x.get_sum.__doc__
    print x.get_sum(3, 7)

if __name__ == "__main__":
    main()