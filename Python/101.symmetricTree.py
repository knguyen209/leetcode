"""
https://leetcode.com/problems/symmetric-tree

Difficulty: Easy
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left and right:
                if left.val == right.val:
                    return dfs(left.left, right.right) and dfs(left.right, right.left)
                else:
                    return False
            elif (left and not right) or (not left and right):
                return False
            else:
                return True
        if not root:
            return True
        
        return dfs(root.left, root.right)