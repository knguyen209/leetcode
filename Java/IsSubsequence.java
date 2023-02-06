import java.util.*;

// https://leetcode.com/problems/is-subsequence
// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting
// some (can be none) of the characters without disturbing the relative positions of the remaining
// characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

public class IsSubsequence {
    public static void main(String[] args) {
        System.out.println(isSubsequence("abc", "ahbgdc")); // true
        System.out.println(isSubsequence("axc", "ahbgdc")); // false
        System.out.println(isSubsequence("", "ahbgdc")); // true
        System.out.println(isSubsequence("acb", "ahbgdc")); // false
    }

    public static boolean isSubsequence(String s, String t) {
        if (s.isEmpty()) {
            return true;
        }

        Queue<Character> charQueue = new LinkedList<>();
        for (char c : s.toCharArray()) {
            charQueue.add(c);
        }

        for (char c : t.toCharArray()) {
            if (!charQueue.isEmpty()) {
                if (c == charQueue.peek()) {
                    charQueue.remove();
                }
            }
        }

        return charQueue.isEmpty();
    }
}
