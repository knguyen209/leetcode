/**
 * Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
 * Return the running sum of nums.
 */

// Input: nums = [1,2,3,4]
// Output: [1,3,6,10]
// Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

public class RunningSum {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        int[] runningSums = runningSum(nums);
        for (int sum : runningSums) {
            System.out.printf("%d\t", sum);
        }
    }

    private static int[] runningSum(int[] nums) {
        int[] runningSums = new int[nums.length];
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            runningSums[i] = sum;
        }

        return runningSums;
    }
}
