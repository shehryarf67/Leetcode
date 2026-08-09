# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root, lower, upper):
            if not root:
                return True

            # Current node must be within its allowed range
            if root.val <= lower or root.val >= upper:
                return False

            # We check if everything less than root and everything greater than root
            # for left and right subtrees
            return (dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper))

        return dfs(root, float("-inf"), float("inf"))