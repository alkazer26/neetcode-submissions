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


        d = prev
        while d:
            print(d.val)
            d= d.next
        
        print()
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
        
        print("NEW", new_head.val) if new_head else None
        print("PREV", prev.val) if prev else None
        c = head
        while c:
            print(c.val)
            c = c.next
        

        