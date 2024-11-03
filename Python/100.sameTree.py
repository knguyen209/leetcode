"""
https://leetcode.com/problems/same-tree/

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameNode(leftNode, rightNode):
            if leftNode and rightNode:
                if leftNode.val == rightNode.val:
                    return isSameNode(leftNode.left, rightNode.left) and isSameNode(leftNode.right, rightNode.right)
                else:
                    return False
            elif (leftNode and not rightNode) or (not leftNode and rightNode):
                return False
            else:
                return True

        return isSameNode(p, q)