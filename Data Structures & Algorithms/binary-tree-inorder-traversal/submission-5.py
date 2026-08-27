# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = []
        cur = root

        while stack or cur:
            # only add left nodes to stack on the way down
            while cur:
                stack.append(cur)
                cur = cur.left
            
            node = stack.pop()
            out.append(node.val)

            if node.right:
                cur = node.right
            
        return out