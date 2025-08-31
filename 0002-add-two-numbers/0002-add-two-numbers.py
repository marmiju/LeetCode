# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0)
        l3 = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1+v2+carry
            carry = value // 10

            rem = value % 10
            new_node = ListNode(rem)

            l3.next = new_node
            l3 = l3.next
            if l1:l1 =l1.next
            if l2: l2 = l2.next
        
        return dummy.next




        

        
        