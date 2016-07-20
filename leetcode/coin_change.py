"""
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

You may assume that you have an infinite number of each kind of coin.
"""
import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :param coins: list of int
        :param amount: int
        :return: int
        """
        minCoins = [0]
        for i in range(1, amount + 1):
            minCoins.append(sys.maxsize)

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i and minCoins[i - coins[j]] + 1 < minCoins[i]:
                    minCoins[i] = minCoins[i - coins[j]] + 1

        if minCoins[amount] == sys.maxsize:
            return -1
        else:
            return minCoins[amount]

if __name__ == "__main__":
    print Solution().coinChange([1, 2, 5], 11)
