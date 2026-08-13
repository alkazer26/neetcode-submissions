# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        def recurse(cur):
            nonlocal newHead
            if cur == None:
                newHead = ListNode()


                return newHead
            
            parent = recurse(cur.next)

            parent.next = cur
            cur.next = None
            return cur  

        recurse(head)

        return newHead.next
