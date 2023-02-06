import java.util.*;

public class SquareRoot {
    public static void main(String[] args) {
        System.out.println(mySqrt(4));
        System.out.println(mySqrt(9));
        System.out.println(mySqrt(8));
    }

    public static int mySqrt(int x) {

        int sqrtX = 0;
        int oddNumber = 1;
        while (x > 0) {
            x = x - oddNumber;
            oddNumber += 2;
            if (x >= 0) {
                sqrtX++;
            }
        }

        return sqrtX;
    }


}
