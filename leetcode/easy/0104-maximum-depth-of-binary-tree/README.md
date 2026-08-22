# Maximum Depth of Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `root` of a binary tree, return  *its maximum depth*.

A binary tree's  **maximum depth**  is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

 **Example 1:** 

```
Input: root = [3,9,20,null,null,15,7]
Output: 3

```

 **Example 2:** 

```
Input: root = [1,null,2]
Output: 2

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 23.30%)  
**Memory:** 26.8 MB (beats 7.98%)  
**Submitted:** 2026-08-22T17:03:11.403Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)