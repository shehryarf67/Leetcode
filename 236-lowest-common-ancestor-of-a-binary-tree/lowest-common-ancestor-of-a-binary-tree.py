# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node is None:
                return None

            # If current node is p or q, return it
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            # p and q found in different subtrees
            if left and right:
                return node

            # Otherwise, propagate whichever side found something
            if left:
                return left

            return right

        return dfs(root)