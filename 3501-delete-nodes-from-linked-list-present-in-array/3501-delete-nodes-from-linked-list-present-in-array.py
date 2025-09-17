# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num_set = set(nums)  # 用 set 提高查找效率
        dummy = ListNode(next=head)
        cur = dummy

        while cur.next:
            if cur.next.val in num_set:   # O(1) 查找
                cur.next = cur.next.next  # 删除节点
            else:
                cur = cur.next            # 保留节点，继续遍历

        return dummy.next
