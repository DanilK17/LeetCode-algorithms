import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root.right or not root.left:
            return sys.maxsize
        return min(root.val - root.left.val, root.right.val - root.val, self.getMinimumDifference(root.left),
                   self.getMinimumDifference(root.right))
