import java.util.HashMap;
import java.util.Map;

/// https://leetcode.com/problems/isomorphic-strings

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

public class IsomorphicStrings {

    public static void main(String[] args) {
        System.out.println(isIsomorphic("add", "egg"));
        System.out.println(isIsomorphic("foo", "bar"));
        System.out.println(isIsomorphic("paper", "title"));
        System.out.println(isIsomorphic("badc", "baba"));
    }

    public static boolean isIsomorphic(String s, String t) {
        return isIso(s, t) && isIso(t, s);
    }

    public static boolean isIso(String s, String t) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                int value = map.get(s.charAt(i));
                if (value != s.charAt(i) - t.charAt(i)) {
                    return false;
                }
            } else {
                map.put(s.charAt(i), s.charAt(i) - t.charAt(i));
            }
        }

        return true;
    }
}
