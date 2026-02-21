import java.util.Objects;
import java.util.Scanner;

public class exercise1_message_analysis {


    
    public static final class Result {
        public final int uppercaseCount;          
        public final int punctuationCount;        
        public final double capsRatio;            
        public final String label;                
        public final boolean repeatedMoreThan3;   

        public Result(int uppercaseCount, int punctuationCount, double capsRatio,
                      String label, boolean repeatedMoreThan3) {
            this.uppercaseCount = uppercaseCount;
            this.punctuationCount = punctuationCount;
            this.capsRatio = capsRatio;
            this.label = Objects.requireNonNull(label);
            this.repeatedMoreThan3 = repeatedMoreThan3;
        }

        @Override
        public String toString() {
            return "Uppercase: " + uppercaseCount
                    + ", Punctuation: " + punctuationCount
                    + ", Caps ratio: " + String.format("%.2f", capsRatio)
                    + " -> " + label
                    + ", Repeat>3: " + repeatedMoreThan3;
        }
    }

    
    public static Result analyze(String message) {
        if (message == null) message = "";

        int upperCount = 0;   
        int alphaCount = 0;   
        int puncCount = 0;    
        boolean hasRepeatSpam = false;

        
        char prev = 0;
        int runLen = 0;
        boolean hasPrev = false;

        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);

            
            if (isAsciiAlphabetic(c)) {
                alphaCount++;
                if (isAsciiUppercase(c)) {
                    upperCount++;
                }
            }

            
            if (c == '!' || c == '?') {
                puncCount++;
            }

        
            if (!hasPrev) {
                runLen = 1;
                hasPrev = true;
            } else if (c == prev) {
                runLen++;
            } else {
                runLen = 1;
            }
            prev = c;

            if (runLen >= 4) {
                hasRepeatSpam = true;
            }
        }

        
        double capsRatio = (alphaCount == 0) ? 0.0 : (upperCount * 1.0 / alphaCount);

       
        String label;
        if (capsRatio >= 0.6 || puncCount >= 5) {
            label = "AGGRESSIVE";
        } else if (capsRatio >= 0.3 || puncCount >= 3) {
            label = "URGENT";
        } else {
            label = "CALM";
        }

        return new Result(upperCount, puncCount, capsRatio, label, hasRepeatSpam);
    }

    
    private static boolean isAsciiAlphabetic(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
    }

    
    private static boolean isAsciiUppercase(char c) {
        return (c >= 'A' && c <= 'Z');
    }

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("EX1 Interactive Analyzer");
        System.out.println("Saisissez un message et appuyez sur Entrée pour démarrer l'analyse; saisissez exit pour quitter.");

        while (true) {
            System.out.print("> ");
            if (!sc.hasNextLine()) break;

            String line = sc.nextLine();

            
            if (line.trim().equalsIgnoreCase("exit")) {
                System.out.println("Bye.");
                break;
            }

            Result r = analyze(line);
            System.out.println(r);
        }

        sc.close();
    }
}