import java.util.HashMap;
import java.util.Map;

public class RomanToInteger {
    public static void main(String[] args) {
        System.out.println("Value of III is " + romanToInt("III"));
        System.out.println("Value of LVIII is " + romanToInt("LVIII"));
        System.out.println("Value of MCMXCIV is " + romanToInt("MCMXCIV"));
    }

    public static int romanToInt(String s) {

        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int sum = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int value = 0;
            char c = s.charAt(i);
            value = map.get(c);

            if (i > 0) {
                char prevChar = s.charAt(i - 1);
                if ((c == 'V' || c == 'X') && prevChar == 'I') {
                    value -= 1;
                    i--;
                }

                if ((c == 'L' || c == 'C') && prevChar == 'X') {
                    value -= 10;
                    i--;
                }

                if ((c == 'D' || c == 'M') && prevChar == 'C') {
                    value -= 100;
                    i--;
                }
            }

            sum += value;
        }
        return sum;
    }
}
