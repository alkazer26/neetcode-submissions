# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        cur1, cur2 = p, q

        # inorder traversal (left, self, right)
        while stack or (cur1 and cur2):
            while cur1 and cur2:
                stack.append((cur1, cur2))
                cur1, cur2 = cur1.left, cur2.left


            if cur1 is not cur2:
                return False
            
            node1, node2 = stack.pop()
            if node1.val != node2.val:
                return False
            
            cur1, cur2 = node1.right, node2.right
        
        return cur1 == cur2

