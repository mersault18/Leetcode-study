# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

    
        if not root:
            return False
        
        # 如果到了叶子节点，判断路径和是否等于 targetSum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 向左右子树递归，更新 targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))