# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q = deque([p])
        q_q = deque([q])

        while p_q and q_q:

            for _ in range(len(p_q)):
                p_node = p_q.popleft()
                q_node = q_q.popleft()

                if p_node and not q_node or not p_node and q_node:
                    return False
        
                if p_node and q_node and p_node.val != q_node.val:
                    return False
                
                if p_node:
                    p_q.append(p_node.left)
                    p_q.append(p_node.right)
                if q_node:
                    q_q.append(q_node.left)
                    q_q.append(q_node.right)

        return True
