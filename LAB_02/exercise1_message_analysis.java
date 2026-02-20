import java.util.Objects;
import java.util.Scanner;

public class exercise1_message_analysis {


    // 用于返回分析结果
    public static final class Result {
        public final int uppercaseCount;          // 大写字母数
        public final int punctuationCount;        // '!' 和 '?' 的总数
        public final double capsRatio;            // uppercase / alphabetic（alphabetic=0 则为 0）
        public final String label;                // CALM / URGENT / AGGRESSIVE
        public final boolean repeatedMoreThan3;   // 是否存在连续重复字符长度 >= 4

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

    /**
     * 分析一条 message（单次扫描）
     */
    public static Result analyze(String message) {
        if (message == null) message = "";

        int upperCount = 0;   // 大写字母数
        int alphaCount = 0;   // 字母总数（ASCII）
        int puncCount = 0;    // ! 和 ? 总数
        boolean hasRepeatSpam = false;

        // 连续重复检测
        char prev = 0;
        int runLen = 0;
        boolean hasPrev = false;

        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);

            // 1) 字母/大写统计（按 ASCII）
            if (isAsciiAlphabetic(c)) {
                alphaCount++;
                if (isAsciiUppercase(c)) {
                    upperCount++;
                }
            }

            // 2) 标点统计：只算 ! 和 ?
            if (c == '!' || c == '?') {
                puncCount++;
            }

            // 3) 连续重复检测：只做相邻字符比较
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

        // 4) caps ratio（避免除 0）
        double capsRatio = (alphaCount == 0) ? 0.0 : (upperCount * 1.0 / alphaCount);

        // 5) 分类（强规则优先）
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

    // 判断是否为 ASCII 字母
    private static boolean isAsciiAlphabetic(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
    }

    // 判断是否为 ASCII 大写字母
    private static boolean isAsciiUppercase(char c) {
        return (c >= 'A' && c <= 'Z');
    }

    /**
     * 交互式入口：
     * - 输入一行字符串，立即输出分析结果
     * - 输入 exit 结束程序
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("EX1 Interactive Analyzer");
        System.out.println("Saisissez un message et appuyez sur Entrée pour démarrer l'analyse; saisissez exit pour quitter.");

        while (true) {
            System.out.print("> ");
            if (!sc.hasNextLine()) break;

            String line = sc.nextLine();

            // 退出条件
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