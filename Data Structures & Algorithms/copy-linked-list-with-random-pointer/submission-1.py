"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_node = head
        old_to_new = {}

        while old_node:
            new_node = Node(old_node.val)
            old_to_new[old_node] = new_node
            old_node = old_node.next

        old_node = head

        while old_node:
            new_node =  old_to_new[old_node]
            new_node.next = old_to_new.get(old_node.next)
            new_node.random = old_to_new.get(old_node.random)
            old_node = old_node.next

        return old_to_new.get(head)

