# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next # n is valid per problem

        # Move both until fast is at the last node
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        # delete the target node
        to_delete = slow.next 
        if to_delete:
            slow.next = to_delete.next
            to_delete.next = None # help gc not required 
        return dummy.next        