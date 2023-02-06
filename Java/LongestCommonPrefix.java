import java.util.*;

// https://leetcode.com/problems/longest-common-prefix/

public class LongestCommonPrefix {
    public static void main(String[] args) {
        System.out.println(longestCommonPrefix(new String[] {"flower", "flow", "flight"}));
        System.out.println(longestCommonPrefix(new String[] {"ab", "a"}));
    }

    public static String longestCommonPrefix(String[] strs) {

        int shortestStrIndex = 0;

        for (int i = 0; i < strs.length; i++) {
            if (strs[i].length() < strs[shortestStrIndex].length()) {
                shortestStrIndex = i;
            }
        }

        String shortestStr = strs[shortestStrIndex];
        System.out.println(shortestStr);

        int subStrIndex = 0;

        for (int i = 0; i < shortestStr.length(); i++) {
            boolean uncommon = false;
            for (String str : strs) {
                if (str.charAt(i) != shortestStr.charAt(i)) {
                    uncommon = true;
                }
            }
            if (uncommon) {
                break;
            } else {
                subStrIndex++;
            }
        }

        return shortestStr.substring(0, subStrIndex);
    }
}
