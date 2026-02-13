import java.util.Scanner;

public class exercise1_integer_mirror{

    /**
     Reverse the decimal digits of a non-negative integer n using only div/mod.
     Example: 315 -> 513, 400 -> 4, 0 -> 0

     Note: This uses long. If the reversed value exceeds Long.MAX_VALUE,
     it will overflow (not handled here unless you add checks).
     */

    public static long integerMirror(long n){
        long r=0;
        while(n>0){
            long digit=n%10;
            r=r*10+digit;
            n=n/10;
        }
        return r;
    }

    public static void main(String[] args){
        // Input style: one non-negative integer
        // Example:
        // Input: 315
        // Output: 513
        Scanner sc=new Scanner(System.in);
        if(!sc.hasNextLong()) return;

        long n=sc.nextLong();
        if(n<0){
            System.out.println("Error: n must be non-negative");
            return;
        }
        System.out.println(integerMirror(n));
    }
}



