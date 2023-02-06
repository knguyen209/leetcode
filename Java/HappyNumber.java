import java.util.*;

// https://leetcode.com/problems/happy-number/

// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a
// cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

public class HappyNumber {
    public static void main(String[] args) {
        System.out.println(isHappy(19));
        System.out.println(isHappy(2));
        System.out.println(isHappy(7));
    }

    public static boolean isHappy(int n) {
        Stack<Integer> digits = getDigits(n);
        List<Integer> seenNumbers = new ArrayList<Integer>();

        int sum = n;

        if (sum == 1) {
            return true;
        }

        while (digits.size() >= 1 && sum != 1) {
            sum = sumSquareDigits(digits);
            digits = getDigits(sum);
            if (seenNumbers.contains(sum)) {
                return false;
            } else {
                seenNumbers.add(sum);
            }
        }

        return sumSquareDigits(getDigits(sum)) == 1;
    }

    private static int sumSquareDigits(Stack<Integer> digits) {
        System.out.println(digits.toString());
        int sum = 0;
        while (!digits.empty()) {
            int digit = digits.pop();
            sum = sum + digit * digit;
        }
        System.out.println("Sum Square: " + sum);
        return sum;
    }

    private static Stack<Integer> getDigits(int n) {
        Stack<Integer> digits = new Stack<Integer>();
        while (n > 0) {
            // if (n % 10 != 0) {


            // }
            digits.push(n % 10);
            n = n / 10;
        }
        return digits;
    }
}
