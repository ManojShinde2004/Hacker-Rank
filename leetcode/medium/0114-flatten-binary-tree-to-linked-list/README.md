# Flatten Binary Tree to Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

 

 **Example 1:** 

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

```

 **Example 2:** 

```
Input: root = []
Output: []

```

 **Example 3:** 

```
Input: root = [0]
Output: [0]

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

 

 **Follow up:**  Can you flatten the tree in-place (with `O(1)` extra space)?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.8 MB (beats 7.87%)  
**Submitted:** 2026-08-30T15:44:11.638Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)