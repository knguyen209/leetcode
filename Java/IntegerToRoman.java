// https://leetcode.com/problems/integer-to-roman/

public class IntegerToRoman {
    public static void main(String[] args) {
        System.out.println(intToRoman(1994));
        // System.out.println(intToRoman(2994));
    }

    public static String intToRoman(int num) {
        String str = "";
        str += getThousandsStr(num);
        num = num % 1000;

        System.out.println(str);

        str += getHundredsStr(num);
        num = num % 100;

        System.out.println(str);

        return str;
    }

    private static String getOnesStr(int num) {
        return "";
    }

    private static String getTensStr(int num) {
        if (num / 10 == 9) {
            return "XC";
        }
        if (num / 10 == 4) {
            return "XL";
        }
        if (num / 10 == 5) {
            return "L";
        }
        return "C".repeat(num / 10);
    }

    private static String getHundredsStr(int num) {
        if (num / 100 == 9) {
            return "CM";
        }
        if (num / 100 == 5) {
            return "CD";
        }
        if (num / 100 == 4) {
            return "D";
        }
        return "C".repeat(num / 100);
    }

    private static String getThousandsStr(int num) {
        return "M".repeat(num / 1000);
    }
}
