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
        