"""https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the
two subtrees of every node never differ by more than 1.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
        if (not self.isBalanced(root.left)) or (not self.isBalanced(root.right)):
            return False

        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if abs(leftDepth - rightDepth) < 2:
            return True
        else:
            return False


    def getDepth(self, root):
        if root == None: return 0
        leftHeight = self.getDepth(root.left)
        rightHeight = self.getDepth(root.right)
        return 1 + max(leftHeight, rightHeight)

