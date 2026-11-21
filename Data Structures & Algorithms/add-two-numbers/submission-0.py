# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2

        count1 = 0
        num1 = 0
        while node1:
            num1 += 10**(count1)*node1.val
            count1 += 1
            node1 = node1.next
        
        count2 = 0
        num2 = 0
        while node2:
            num2 += 10**(count2)*node2.val
            count2 += 1
            node2 = node2.next
        
        sum = num1+num2
        length = len(str(sum)) 

        num_list = []
        for i in range(length):
            power = length-i-1
            num = (sum//(10**power))%10
            num_list.append(num)
        num_list.reverse()

        dummy = ListNode(0)
        curr = dummy

        for i in num_list:
            curr.next = ListNode(i)
            curr = curr.next
            
        return dummy.next
