import java.util.Stack;

public class ValidParentheses {
    public static void main(String[] args) {
        System.out.println(isValid("())"));
        System.out.println(isValid("()"));
        System.out.println(isValid("(])"));
    }

    public static boolean isValid(String s) {
        Stack<Character> charStack = new Stack<Character>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                charStack.push(c);
            }

            if (c == ')') {
                if (charStack.size() > 0) {
                    if (charStack.peek().charValue() == '(') {
                        charStack.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
            if (c == ']') {
                if (charStack.size() > 0) {
                    if (charStack.peek().charValue() == '[') {
                        charStack.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
            if (c == '}') {
                if (charStack.size() > 0) {
                    if (charStack.peek().charValue() == '{') {
                        charStack.pop();
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }

        return charStack.size() == 0;
    }

    // public static boolean isValid(String s) {
    // int noOpenRoundParentheses = 0;
    // int noOpenSquareParentheses = 0;
    // int noOpenPointyParentheses = 0;
    // int noCloseRoundParentheses = 0;
    // int noCloseSquareParentheses = 0;
    // int noClosePointyParentheses = 0;


    // for (char c : s.toCharArray()) {
    // if (c == '(') {
    // noOpenRoundParentheses++;
    // }
    // if (c == ')') {
    // noCloseRoundParentheses++;
    // }
    // if (c == '{') {
    // noOpenPointyParentheses++;
    // }
    // if (c == '}') {
    // noClosePointyParentheses++;
    // }
    // if (c == '[') {
    // noOpenSquareParentheses++;
    // }
    // if (c == ']') {
    // noCloseSquareParentheses++;
    // }

    // }

    // if (noOpenRoundParentheses == noCloseRoundParentheses
    // && noOpenSquareParentheses == noCloseSquareParentheses
    // && noOpenPointyParentheses == noClosePointyParentheses) {
    // return true;
    // }

    // return false;
    // }
}
