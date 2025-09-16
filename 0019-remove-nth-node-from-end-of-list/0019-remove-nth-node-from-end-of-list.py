# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next = head)
        right = dummy
        for _ in range(n):
            right = right.next

        left = dummy
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        