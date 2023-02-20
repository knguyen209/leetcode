// https://leetcode.com/problems/find-the-duplicate-number/description/
import java.util.*;

public class FindDuplicate {
    public static void main(String[] args) {
        System.out.println("Duplicate: " + findDuplicate(new int[] {1, 2, 3, 4, 4}));
        System.out.println("Duplicate: " + findDuplicate(new int[] {4, 4, 1, 2, 3}));
        System.out.println("Duplicate: " + findDuplicate(new int[] {1, 3, 4, 2, 2}));
    }

    public static int findDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                return nums[i];
            } else {
                map.put(nums[i], 1);
            }
        }
        return nums.length;
    }
}
