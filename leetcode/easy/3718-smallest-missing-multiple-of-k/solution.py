class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=1
        while True:
            
            for i in range(len(nums)):
                if(nums[i]==k*count):
                    break
                elif(i==len(nums)-1):
                    return k*count
                    
                else:
                    continue 
            count+=1

            
        