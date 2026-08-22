class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_len = [0]

        def depth(tmp_max, root):
            if root is None:
                return

            tmp_max += 1

            if root.left is None and root.right is None:
                if tmp_max > max_len[0]:
                    max_len[0] = tmp_max
                return

            depth(tmp_max, root.left)
            depth(tmp_max, root.right)

        depth(0, root)

        return max_len[0]