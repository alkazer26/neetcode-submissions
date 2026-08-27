class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        cur1, cur2 = p, q

        while stack or cur1 or cur2:
            # Keep moving left on both trees
            while cur1 and cur2:
                stack.append((cur1, cur2))
                cur1, cur2 = cur1.left, cur2.left

            # If one reached None while the other didn't, structural mismatch!
            if cur1 or cur2:
                return False

            node1, node2 = stack.pop()
            
            # Value mismatch check
            if node1.val != node2.val:
                return False

            # Move to right subtrees
            cur1, cur2 = node1.right, node2.right

        return True