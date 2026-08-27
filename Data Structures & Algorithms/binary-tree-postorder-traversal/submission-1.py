# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        out = []

        while stack or cur:
            while cur:
                stack.append([cur, False])
                cur = cur.left

            node, visited = stack[-1]
            if visited or not node.right:
                node, _ = stack.pop()
                out.append(node.val)
            else:
                stack[-1][1] = True
                cur = node.right
        
        return out
