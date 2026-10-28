
class Solution {
    public int dominantIndex(int[] nums) {
        int max1 = -1;
        int max2 = -1;
        int max_index = -1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > max1) {
                max2 = max1;
                max1 = nums[i];
                max_index = i;
            } else if (nums[i] > max2) {
                max2 = nums[i];
            }
        }

        if (max2 * 2 <= max1) {
            return max_index;
        }

        return -1;
    }
}
