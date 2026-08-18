# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        cur = root

        while stack:
            while cur and cur.right:
                stack.append(cur.right)
                cur = cur.right
            
            last = stack.pop()
            print(last.val)
            cur = last.left
            last.left, last.right = last.right, last.left
 
            if cur:
                stack.append(cur)
            
        
        return root
            












        # def recurse(node):
        #     if not node:
        #         return None
            
        #     left = recurse(node.right)
        #     right = recurse(node.left)

        #     node.left = left
        #     node.right = right

        #     return node
        
        # recurse(root)

        # return root