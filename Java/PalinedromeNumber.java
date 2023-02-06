public class PalinedromeNumber {
    public static void main(String[] args) {
        System.out.println(isPalindrome(121));
    }

    public static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        if (x >= 0 && x < 10) {
            return true;
        }

        String strX = String.valueOf(x);

        boolean isPalindrome = true;

        for (int i = 0; i < strX.length() / 2; i++) {
            if (strX.charAt(i) != strX.charAt(strX.length() - 1 - i)) {
                isPalindrome = false;
                return isPalindrome;
            }
        }
        return isPalindrome;
    }
}
