# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # TODO: implement recursive DFS, each time we reach base case increment idx, check idx == k?
        # implement BFS, somehow count the idx? store it in the bfs queue? idk.
        idx = 0
        kth = None

        def recurse(node):
            nonlocal idx
            nonlocal k
            nonlocal kth

            if not node or kth:
                return 
            
            recurse(node.left)

            idx += 1

            if idx == k:
                kth = node.val
                return

            recurse(node.right)
        
        recurse(root)

        return kth
