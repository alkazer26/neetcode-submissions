# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        newHead = None
        def recurse(cur):
            nonlocal newHead
            if cur == None:
                newHead = ListNode()
                return newHead
            
            parent = recurse(cur.next)

            parent.next = cur
            return cur  

        recurse(head)
        head.next = None

        return newHead.next
