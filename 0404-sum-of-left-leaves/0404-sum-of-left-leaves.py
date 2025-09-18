# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, is_left):
            if not node:
                return 0
            # 如果是叶子且为左节点，返回它的值
            if not node.left and not node.right and is_left:
                return node.val
            # 否则递归左右子树并相加
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
