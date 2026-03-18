
import java.util.Arrays;

public class exercise2_recursive_aggregation {

    static class Post {
        int postId;
        int likes;
        int comments;
        int shares;
        int engagement;

        public Post(int postId, int likes, int comments, int shares) {
            this.postId = postId;
            this.likes = likes;
            this.comments = comments;
            this.shares = shares;
            this.engagement = likes + 2 * comments + 3 * shares;
        }

        public String toString() {
            return "(" + postId + ":" + engagement + ")";
        }
    }

    // Part A: Maximum Engagement
    public static int maxEngagement(Post[] p, int l, int r) {
        if (l == r) return p[l].engagement;

        int m = (l + r) / 2;

        int a = maxEngagement(p, l, m);
        int b = maxEngagement(p, m + 1, r);

        return Math.max(a, b);
    }

    // Part B: Sum Engagement
    public static int sumEngagement(Post[] p, int l, int r) {
        if (l == r) return p[l].engagement;

        int m = (l + r) / 2;

        return sumEngagement(p, l, m) + sumEngagement(p, m + 1, r);
    }

    // Part B: Average Engagement
    public static double avgEngagement(Post[] p, int l, int r) {
        int sum = sumEngagement(p, l, r);
        return (double) sum / (r - l + 1);
    }

    // Part C: Count Above Threshold
    public static int countAbove(Post[] p, int l, int r, int t) {
        if (l == r) return p[l].engagement > t ? 1 : 0;

        int m = (l + r) / 2;

        return countAbove(p, l, m, t) + countAbove(p, m + 1, r, t);
    }

    // Part D: Merge Sort by Engagement
    public static void mergeSort(Post[] p, int l, int r) {
        if (l >= r) return;

        int m = (l + r) / 2;

        mergeSort(p, l, m);
        mergeSort(p, m + 1, r);

        merge(p, l, m, r);
    }

    // Part D: Merge Function
    public static void merge(Post[] p, int l, int m, int r) {
        Post[] temp = new Post[r - l + 1];

        int i = l, j = m + 1, k = 0;

        while (i <= m && j <= r) {
            if (p[i].engagement <= p[j].engagement) {
                temp[k++] = p[i++];
            } else {
                temp[k++] = p[j++];
            }
        }

        while (i <= m) temp[k++] = p[i++];
        while (j <= r) temp[k++] = p[j++];

        for (int x = 0; x < temp.length; x++) {
            p[l + x] = temp[x];
        }
    }

    // Part E: Find Peak Hour
    public static int peak(int[] a, int l, int r) {
        if (l == r) return l;

        int m = (l + r) / 2;

        if (a[m] < a[m + 1]) {
            return peak(a, m + 1, r);
        } else {
            return peak(a, l, m);
        }
    }

    public static void main(String[] args) {

        Post[] p = {
                new Post(1, 50, 20, 20),
                new Post(2, 100, 40, 47),
                new Post(3, 35, 15, 10),
                new Post(4, 70, 40, 43)
        };

        System.out.println(Arrays.toString(p));

        System.out.println("max = " + maxEngagement(p, 0, p.length - 1));
        System.out.println("sum = " + sumEngagement(p, 0, p.length - 1));
        System.out.println("avg = " + avgEngagement(p, 0, p.length - 1));
        System.out.println("count >200 = " + countAbove(p, 0, p.length - 1, 200));

        mergeSort(p, 0, p.length - 1);
        System.out.println(Arrays.toString(p));

        int[] likes = {5, 8, 12, 25, 30, 28, 15, 10};
        int idx = peak(likes, 0, likes.length - 1);

        System.out.println("peak index = " + idx);
    }
}