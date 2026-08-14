# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split array in two (first iteration)
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow.next
        slow.next = None
        slow = tmp

        # now head = head of first half, slow = head of second half
        # reverse second half
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # prev stores head of reversed list
        # interleave both halves
        new_head = head
        while new_head and prev:
            nxt_1 = new_head.next
            new_head.next = prev

            nxt_2 = prev.next
            prev.next = nxt_1

            new_head = nxt_1
            prev = nxt_2

        

        