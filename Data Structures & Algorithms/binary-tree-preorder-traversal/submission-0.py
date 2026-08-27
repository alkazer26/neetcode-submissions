# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                out.append(cur.val)
                cur = cur.left

            node = stack.pop()
            if node.right:
                cur = node.right
            
        
        return out
                