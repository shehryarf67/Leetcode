# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None

        # First preorder element is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find root in inorder
        mid = inorder.index(root_val)

        # Everything left of mid belongs to left subtree
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )

        # Everything right of mid belongs to right subtree
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root

        # Also a hashmap solution. 