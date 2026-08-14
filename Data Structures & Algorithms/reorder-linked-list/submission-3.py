# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        def recurse(node):
            nonlocal cur
            if not node or not node.next:
                return node

            tail = recurse(node.next)
            if not tail:
                return None

            if cur == tail:
                cur.next = None
                return None
            elif cur.next == tail: # <--- Split this check:
                tail.next = None   # Fix: terminate AFTER tail on even lengths!
                return None
            else:
                nxt = cur.next
                cur.next = tail
                tail.next = nxt
                cur = nxt

            return node
        
        recurse(head)
        