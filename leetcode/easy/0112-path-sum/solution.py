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
        
        def mysum(r, total):

            if r is None:
                return False

            total += r.val

            if r.left is None and r.right is None:
                return total == targetSum

            return mysum(r.left, total) or mysum(r.right, total)

        return mysum(root, 0)



        
            
        