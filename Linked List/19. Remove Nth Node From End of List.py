# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        count=0

        while curr:
            curr=curr.next
            count+=1

        i=count-n

        if i==0: return head.next

        curr=head

        for _ in range(i-1):
            curr=curr.next

        curr.next=curr.next.next

        return head
        
        
