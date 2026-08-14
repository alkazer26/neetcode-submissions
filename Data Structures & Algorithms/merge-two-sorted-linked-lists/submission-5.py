# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy

        head1, head2 = list1, list2

        cur = dummy 
        def recurse(l1, l2):
            nonlocal cur
            if not l1 and not l2:
                return
                
            if not l1 and l2:
                cur.next = l2
                cur = cur.next
                recurse(l1, l2.next)
            elif not l2 and l1:
                cur.next = l1
                cur = cur.next
                recurse(l1.next, l2)
            elif l1.val > l2.val:
                cur.next = l2
                cur = cur.next
                recurse(l1, l2.next)
            else:
                cur.next = l1
                cur = cur.next
                recurse(l1.next, l2)
            
        recurse(list1, list2)
        return dummy.next