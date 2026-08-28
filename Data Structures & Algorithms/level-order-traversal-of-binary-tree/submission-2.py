# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []

        def recurse(node, depth):
            if not node:
                return []
            
            if len(out) <= depth:
                out.append([node.val])
            else:
                out[depth].append(node.val)
            
            recurse(node.left, depth + 1)
            recurse(node.right, depth + 1)
        
        recurse(root, 0)
        return out

