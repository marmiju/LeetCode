# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head

        # two pointer for devide two part left and right
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now traverse list

        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # compare 
        left,right= head,prev
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True

        