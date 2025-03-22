# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        head = l3
        carry = 0
        prev = None
        while l1 and l2:
            cur = l1.val + l2.val + carry
            carry = cur // 10
            rem = cur % 10
            l3.val = rem
            l1 = l1.next
            l2 = l2.next
            prev = l3
            l3.next = ListNode()
            l3 = l3.next
            
        
        if l1:
            while l1:
                cur = l1.val + carry
                carry = cur // 10
                rem = cur % 10
                l3.val = rem
                l1 = l1.next
                prev = l3
                l3.next = ListNode()
                l3 = l3.next

        elif l2:
            while l2:
                cur = l2.val + carry
                carry = cur // 10
                rem = cur % 10
                l3.val = rem
                l2 = l2.next
                prev = l3
                l3.next = ListNode()
                l3 = l3.next
        
        if carry:
            l3.val = carry
        else:
            prev.next = None
        return head


        