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
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while True:            
            if head2.val != head.val:
                return False
            
            if head2 is mid:
                break
            head2 = head2.next
            head = head.next

        return True
