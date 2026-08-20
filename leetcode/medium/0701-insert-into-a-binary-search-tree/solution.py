# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            root=TreeNode(val)
        def traverse(root):
            if root is None:
                return
            if root.left is None and val<root.val:
                new_node=TreeNode(val)
                root.left=new_node

            if root.right is None and val>root.val:
                new_node=TreeNode(val)
                root.right=new_node

            if val>root.val:
                traverse(root.right)
            else:
                traverse(root.left)
            
        traverse(root)
            
        return root

        