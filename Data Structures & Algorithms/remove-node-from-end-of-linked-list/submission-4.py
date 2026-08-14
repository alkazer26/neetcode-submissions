# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def recurse(node):
            if node == None:
                return 0
            
            n_rem = 1 + recurse(node.next)
            
            if n_rem == n + 1:
                print(node.val)
                node.next = node.next.next  

            return n_rem

        dummy = ListNode()
        dummy.next = head
        recurse(dummy)

        return dummy.next
        

            
