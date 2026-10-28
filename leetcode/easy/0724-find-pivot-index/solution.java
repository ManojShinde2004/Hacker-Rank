class Solution {
    public int pivotIndex(int[] nums) {
        int sum=0;
        int left=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];

       }
       int index;


      for(index=0;index<nums.length;index++){
        sum=sum-nums[index];
        
        if(left==sum){
            return index;

        }
        left=left+nums[index];
       
        
       }
        
        return -1;
    }
    
}