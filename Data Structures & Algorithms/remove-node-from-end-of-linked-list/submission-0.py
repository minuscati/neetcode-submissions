# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # step1: calculate length
        curr = head
        len_l = 0

        while curr:
            curr = curr.next
            len_l += 1

        # step2: create dummy node
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        new_curr = head

        for _ in range(len_l-n):
            prev = new_curr
            new_curr = new_curr.next

        prev.next = new_curr.next

        return dummy.next

        