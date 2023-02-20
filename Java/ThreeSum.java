// https://leetcode.com/problems/3sum/
import java.util.*;

public class ThreeSum {
    public static void main(String[] args) {
        // System.out.println(threeSum(new int[] {-1, 0, 1, 2, -1, -4}));
        System.out.println(threeSum(new int[] {34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52,
                -3, 93, 15, 21, -43, 57, -6, 86, 56, 94, 74, 83, -14, 28, -66, 46, -49, 62, -11, 43,
                65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29, 36, -29, 10, -70, 69,
                17, 49}));
        // System.out.println(threeSum(new int[] {0, 1, 1}));
        // System.out.println(threeSum(new int[] {0, 0, 0}));
    }

    public static List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> results = new ArrayList<>();

        List<Integer> negatives = new ArrayList<>();
        List<Integer> zeros = new ArrayList<>();
        List<Integer> positives = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 0) {
                negatives.add(nums[i]);
            }
            if (nums[i] == 0) {
                zeros.add(nums[i]);
            }
            if (nums[i] > 0) {
                positives.add(nums[i]);
            }
        }

        Collections.sort(negatives);
        Collections.sort(positives);

        System.out.println(negatives.toString());
        System.out.println(zeros.toString());
        System.out.println(positives.toString());

        if (zeros.size() > 0) {
            for (int i = 0; i < negatives.size(); i++) {
                int neg = negatives.get(i);
                if (positives.contains(neg * -1)
                        && !results.contains(Arrays.asList(neg, 0, neg * -1))) {
                    results.add(Arrays.asList(neg, 0, neg * -1));
                }
            }
        }

        if (zeros.size() >= 3) {
            results.add(Arrays.asList(0, 0, 0));
        }

        for (int i = 0; i < negatives.size(); i++) {
            for (int j = i + 1; j < negatives.size(); j++) {
                int target = (negatives.get(i) + negatives.get(j)) * -1;
                List<Integer> targetList =
                        Arrays.asList(negatives.get(i), negatives.get(j), target);
                if (positives.contains(target) && !results.contains(targetList)) {
                    results.add(Arrays.asList(negatives.get(i), negatives.get(j), target));
                }
            }
        }

        for (int i = 0; i < positives.size(); i++) {
            for (int j = i + 1; j < positives.size(); j++) {
                int target = (positives.get(i) + positives.get(j)) * -1;
                List<Integer> targetList =
                        Arrays.asList(target, positives.get(i), positives.get(j));
                if (negatives.contains(target) && !results.contains(targetList)) {
                    results.add(targetList);
                }
            }
        }

        return results;
    }
    // public static List<List<Integer>> threeSum(int[] nums) {
    // List<List<Integer>> results = new ArrayList<>();

    // for (int i = 0; i < nums.length; i++) {
    // for (int j = i + 1; j < nums.length; j++) {
    // if (i != j) {
    // for (int k = j + 1; k < nums.length; k++) {
    // if (j != k && i != k) {
    // System.out.printf("i = %d, j = %d, k = %d, sum = %d\n", nums[i],
    // nums[j], nums[k], nums[i] + nums[j] + nums[k]);
    // if (nums[i] + nums[j] + nums[k] == 0) {
    // List<Integer> list = new ArrayList<>();
    // list.add(nums[i]);
    // list.add(nums[j]);
    // list.add(nums[k]);

    // Collections.sort(list);

    // if (!results.contains(list)) {
    // results.add(list);
    // }
    // }
    // }
    // }
    // }
    // }
    // }

    // return results;
    // }
}
