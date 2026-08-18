# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recurse(node):
            if not node:
                return None
            
            left = recurse(node.right)
            right = recurse(node.left)

            node.left = left
            node.right = right

            return node
        
        recurse(root)

        return root