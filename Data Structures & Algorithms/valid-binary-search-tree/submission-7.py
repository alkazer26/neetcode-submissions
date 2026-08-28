# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurse(node, lower, upper):

            if node and (node.val >= upper or node.val <= lower):
                return False

            if not node:
                return True

            return recurse(node.left, lower, node.val) and recurse(node.right, node.val, upper)

        return recurse(root, float("-inf"), float("inf"))
