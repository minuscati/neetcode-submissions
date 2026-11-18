# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# 两种解法-迭代、递归
# 迭代法，双指针
        prev = None
        current = head

        while current:
            next_node = current.next

            current.next = prev

            prev = current
            current = next_node

        return prev