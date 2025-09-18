# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        # 如果左子树为空，只能走右子树
        if root.left is None:
            return self.minDepth(root.right) + 1
        # 如果右子树为空，只能走左子树
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # 两边都不为空，取较小值
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1