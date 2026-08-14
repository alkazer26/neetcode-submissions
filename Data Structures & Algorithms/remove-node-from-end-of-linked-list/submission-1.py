# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0-indexed node to remove = length of list - n
        if head.next == None:
            return None

        # compute length of list
        l_len = 0
        cur = head
        while cur:
            l_len += 1
            cur = cur.next
        
        r_idx = l_len - n

        cur_idx = 0
        cur = ListNode()
        dummy = cur
        cur.next = head

        while cur_idx < r_idx:
            cur = cur.next
            cur_idx += 1

        cur.next = cur.next.next

        return dummy.next