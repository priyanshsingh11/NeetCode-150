# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        current=dummy
        carry=0

        while l1 or l2:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            digit=val1+val2+carry
            carry=digit//10

            current.next=ListNode(digit%10)
            current=current.next

            if l1: l1=l1.next
            if l2: l2=l2.next

            if carry:
                current.next=ListNode(carry)

        return dummy.next
