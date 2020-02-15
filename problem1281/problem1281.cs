public class Solution {
    public int SubtractProductAndSum(int n) {
        int s = 0;
        int m = 1;

        while (n > 0) {
            s += n % 10;
            m *= n % 10;
            n /= 10;
        }
        return m - s;
	}
}