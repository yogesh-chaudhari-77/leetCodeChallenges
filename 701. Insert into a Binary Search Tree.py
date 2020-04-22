"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST.
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root.val > val :
            if root.left is None :
                root.left = TreeNode(val)
            else :
                self.insertIntoBST(root.left, val)

        elif root.val < val :
            if root.right is None :
                root.right = TreeNode(val)
            else :
                self.insertIntoBST(root.right, val)

        return root;