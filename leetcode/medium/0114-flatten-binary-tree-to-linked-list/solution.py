class Solution(object):
    def flatten(self, root):
        if root is None:
            return

        prev = [None]

        def traverse(node):
            if node is None:
                return

            
            left = node.left
            right = node.right

            if prev[0] is not None:
                prev[0].left = None
                prev[0].right = node

            prev[0] = node

            traverse(left)
            traverse(right)

        traverse(root)