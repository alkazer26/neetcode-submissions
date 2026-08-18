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
            
        q = deque([root])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                l, r = None, None
                if cur.left:
                    r = cur.left
                    q.append(cur.left)
                if cur.right:
                    l = cur.right
                    q.append(cur.right)

                cur.left = l
                cur.right = r

        return root
