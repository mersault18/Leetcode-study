# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        def f(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            
            # 两种情况：不翻转 / 翻转
            no_flip = f(node1.left, node2.left) and f(node1.right, node2.right)
            flip = f(node1.left, node2.right) and f(node1.right, node2.left)
            
            return no_flip or flip
        
        return f(root1, root2)
