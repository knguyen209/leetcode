import java.util.*;

// https://leetcode.com/problems/missing-number/description/

// Given an array nums containing n distinct numbers in the range [0, n], return the only number in
// the range that is missing from the array.

public class MissingNumber {
    public static void main(String[] args) {
        System.out.println(missingNumber(new int[] {3, 0, 1}));
        System.out.println(missingNumber(new int[] {9, 6, 4, 2, 3, 5, 7, 0, 1}));
    }


    public static int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = (n * (n + 1)) / 2;

        for (int i = 0; i < nums.length; i++) {
            sum -= nums[i];
        }

        return sum;
    }
    // Complexity n^2
    // public static int missingNumber(int[] nums) {
    // for (int i = 0; i < nums.length; i++) {
    // boolean found = false;
    // for (int j = 0; j < nums.length; j++) {
    // if (i == nums[j]) {
    // found = true;
    // }
    // }
    // if (found == false) {
    // return i;
    // }
    // }

    // return nums.length;
    // }
}
