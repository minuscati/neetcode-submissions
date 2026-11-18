# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
# Hashset
        seen = set()
        node1 = head

        while node1:
            # seen.append(node1)
            if node1 in seen:
                return True

            seen.add(node1)
            node1 = node1.next

        return False