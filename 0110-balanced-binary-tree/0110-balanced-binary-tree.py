# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def get_height(node):
            if node is None:
                return 0
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            right_height = get_height(node.right)
            if right_height == -1 or abs(left_height - right_height) >1:
                return -1
            return max(left_height, right_height) + 1
        return get_height(root) != -1