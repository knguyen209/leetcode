// Given an array of integers nums, calculate the pivot index of this array.

// The pivot index is the index where the sum of all the numbers strictly to the left of the index
// is equal to the sum of all the numbers strictly to the index's right.

// If the index is on the left edge of the array, then the left sum is 0 because there are no
// elements to the left. This also applies to the right edge of the array.

// Return the leftmost pivot index. If no such index exists, return -1.

// https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1



public class FindPivotIndex {
    public static void main(String[] args) {
        int[] nums = {-1, -1, 0, 0, -1, -1};
        System.out.printf("Pivot Index: %d\n", pivotIndex(nums));
    }

    public static int pivotIndex(int[] nums) {

        for (int i = 0; i < nums.length; i++) {
            int leftSum = calculateLeftSum(nums, i);
            int rightSum = calculateRightSum(nums, i);
            if (leftSum == rightSum) {
                return i;
            }
        }
        return -1;
    }

    private static int calculateLeftSum(int[] nums, int pivotIndex) {
        int sum = 0;

        for (int i = 0; i < pivotIndex; i++) {
            sum += nums[i];
        }

        return sum;
    }

    private static int calculateRightSum(int[] nums, int pivotIndex) {
        int sum = 0;
        if (pivotIndex < nums.length - 1) {
            for (int i = pivotIndex + 1; i < nums.length; i++) {
                sum += nums[i];
            }
        }
        return sum;
    }
}
