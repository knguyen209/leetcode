import java.util.*;

// https://leetcode.com/problems/single-number/

// Given a non-empty array of integers nums, every element appears twice except for one. Find that
// single one.

// You must implement a solution with a linear runtime complexity and use only constant extra space.

public class SingleNumber {

    public static void main(String[] args) {
        System.out.println("R: " + singleNumber(new int[] {2, 2, 1})); // 1
        System.out.println("R: " + singleNumber(new int[] {4, 1, 2, 1, 2})); // 4

    }

    // Using Exclusive OR
    public static int singleNumber(int[] nums) {
        int singleNum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            singleNum ^= nums[i];
        }
        return singleNum;
    }

    // Using Hashmap
    // public static int singleNumber(int[] nums) {
    // Map<Integer, Integer> history = new HashMap<Integer, Integer>();
    // for (int i = 0; i < nums.length; i++) {
    // if (history.get(nums[i]) != null) {
    // history.put(nums[i], history.get(nums[i]) + 1);
    // } else {
    // history.put(nums[i], 1);
    // }
    // }
    // System.out.println(history.toString());
    // for (Integer num : history.keySet()) {
    // if (history.get(num) == 1) {
    // return num;
    // }
    // }
    // return -1;
    // }
}
