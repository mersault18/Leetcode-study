# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        maxs = head2.val + head.val
        while head2 is not mid:
            head = head.next
            head2 = head2.next
            summ = head2.val + head.val
            if summ > maxs:
                maxs = summ
            

        return maxs
