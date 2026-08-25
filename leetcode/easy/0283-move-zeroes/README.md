# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 28.44%)  
**Memory:** 13.3 MB (beats 97.70%)  
**Submitted:** 2026-08-25T16:56:54.911Z  

```py
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while(r!=len(nums)):
            if(nums[l]>0 or nums[l]<0):
                l+=1
                r+=1
                continue
            elif((nums[r]>0 or nums[r]<0) and nums[l]==0):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1
                continue
            else:
                r+=1
        return nums
        
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)