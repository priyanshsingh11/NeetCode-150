# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
    def reorderList(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second_half = self.reverseList(slow.next)
        slow.next = None

        curr1=head
        curr2=second_half

        while curr2:
            temp1=curr1.next
            temp2=curr2.next

            curr1.next=curr2
            curr2.next=temp1

            curr1=temp1
            curr2=temp2

        return head

        
