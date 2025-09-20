# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def f(node, depth):
            if node is None:
                return 
            if depth == len(ans):
                ans.append(node.val)

            f(node.right, depth+1)
            f(node.left, depth+1)

        f(root, 0)
        return ans
