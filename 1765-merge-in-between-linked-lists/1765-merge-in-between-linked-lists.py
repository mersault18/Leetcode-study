# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        head = list1
        cur = head

        # 1. 找到第 a-1 个节点
        for _ in range(a-1):
            cur = cur.next
        left = cur

        # 2. 找到第 b+1 个节点
        right = cur
        for _ in range(b-a+2):
            right = right.next

        # 3. 接上 list2
        left.next = list2

        # 4. 找到 list2 的尾节点
        tail = list2
        while tail.next:
            tail = tail.next

        # 5. 把尾巴接回去
        tail.next = right

        return head
