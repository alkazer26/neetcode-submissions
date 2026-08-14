# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def recurse(node, total):
            nonlocal n
            if node == None:
                return total - 1
            
            N = recurse(node.next, total + 1)

            if N - total == n:
                node.next = node.next.next
                return -1
            
            return N

        dummy = ListNode()
        dummy.next = head
        recurse(dummy, 0)

        return dummy.next
        

            
