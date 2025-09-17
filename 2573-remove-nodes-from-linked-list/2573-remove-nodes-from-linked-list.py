# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
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
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head2 = self.reverseList(head)
        cur = head2
        maxn = head2.val
        while cur.next:
            if cur.next.val < maxn:
                cur.next = cur.next.next
            else:
                maxn = cur.next.val
                cur = cur.next
        head3 = self.reverseList(head2)
        return head3
