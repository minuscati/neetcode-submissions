# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# 递归法
        def recur(cur, pre):
            if not cur: return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)