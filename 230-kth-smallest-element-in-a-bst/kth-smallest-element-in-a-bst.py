# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nodes = []

        def dfs(node):
            if not node:
                return

            nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        nodes.sort()
        return nodes[k - 1]