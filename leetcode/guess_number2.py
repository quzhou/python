"""https://leetcode.com/problems/guess-number-higher-or-lower-ii/
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when
you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""

# MiniMax

class Solution(object):
    def get_money_amount(self, n):
        """
        :param n: int
        :return: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        y = get_money_amount(n - 1)


