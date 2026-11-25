# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slowP = head
        fastP = head.next
        i = 0
        while fastP:
            if fastP.next == slowP:
                return True
            slowP = slowP.next
            fastP = fastP.next
            if fastP:
                fastP = fastP.next

        return False
