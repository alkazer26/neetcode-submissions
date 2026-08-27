# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        out = []
        
        last_visited = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            peek_node = stack[-1]

            if last_visited is not peek_node.right and peek_node.right:
                cur = peek_node.right
            else:
                last_visited = peek_node
                out.append(stack.pop().val)

        return out
