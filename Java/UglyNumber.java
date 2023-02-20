// https://leetcode.com/problems/ugly-number

public class UglyNumber {
    public static void main(String[] args) {
        System.out.println(isUgly(6));
    }

    public static boolean isUgly(int n) {
        if (n <= 0) {
            return false;
        }

        while (n % 2 == 0) {
            n = n / 2;
        }

        while (n % 3 == 0) {
            n = n / 3;
        }

        while (n % 5 == 0) {
            n = n / 5;
        }

        if (n == 1) {
            return true;
        } else {
            return false;
        }
    }
}
