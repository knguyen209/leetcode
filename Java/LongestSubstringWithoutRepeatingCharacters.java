// https://leetcode.com/problems/longest-substring-without-repeating-characters/

public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        LongestSubstringWithoutRepeatingCharacters main =
                new LongestSubstringWithoutRepeatingCharacters();
        String s = "abcabcbb";
        System.out.println(main.lengthOfLongestSubstring(s));
    }

    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            int length = 0;
            char c = s.charAt(i);
            for (int j = i + 1; j < s.length(); j++) {
                char duplicateChar = s.charAt(j);
                if (c == duplicateChar) {
                    length = j - i;
                    if (length > maxLength) {
                        maxLength = length;
                    }

                }
            }
        }
        return maxLength;
    }
}
