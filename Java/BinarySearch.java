// https://leetcode.com/problems/binary-search/

public class BinarySearch {
    public static void main(String[] args) {
        // System.out.println(search(new int[] {-1, 0, 3, 5, 9, 12}, 9));
        System.out.println(search(new int[] {-1, 0, 3, 5, 9, 12}, 2));
    }

    public static int search(int[] nums, int target) {
        return search(nums, target, 0, nums.length - 1);
    }

    private static int search(int[] nums, int target, int startIndex, int endIndex) {
        if (startIndex > endIndex) {
            return -1;
        }

        int midIndex = (startIndex + endIndex) / 2;

        if (nums[midIndex] == target) {
            return midIndex;
        }

        if (nums[midIndex] > target) {
            return search(nums, target, startIndex, midIndex - 1);
        }

        if (nums[midIndex] < target) {
            return search(nums, target, midIndex + 1, endIndex);
        }

        return -1;
    }
}
