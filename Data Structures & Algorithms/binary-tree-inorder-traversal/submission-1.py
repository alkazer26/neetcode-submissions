# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        stack = [root]

        visited = {root}
        while stack:
            cur = stack[-1]
            if cur.left and cur.left not in visited:
                stack.append(cur.left)
                visited.add(cur.left)
            else:
                node = stack.pop()
                out.append(node.val)
                if node.right:
                    stack.append(node.right)


        return out