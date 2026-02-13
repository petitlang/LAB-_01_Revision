package LAB_01;
import java.util.Locale;
import java.util.Scanner;

public class exercise4_polynomial_eval {
    // coeffs[i] is the coefficient of x^i
    // Horner: evaluate in O(n)
    public static double hornerEval(double[] coeffs, double x) {
        double result = 0.0;
        for (int i = coeffs.length - 1; i >= 0; i--) {
            result = result * x + coeffs[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        // coeffs[0] coeffs[1] ... coeffs[m-1]

        if (!sc.hasNextInt()) return;
        int m = sc.nextInt();

        if (m <= 0) {
            System.out.println(0.0);
            return;
        }
        double[] coeffs = new double[m];
        for (int i = 0; i < m; i++) {
            if (!sc.hasNextDouble()) return;
            coeffs[i] = sc.nextDouble();
        }

        if (!sc.hasNextDouble()) return;
        double x = sc.nextDouble();

        System.out.println(hornerEval(coeffs, x));

    }
}