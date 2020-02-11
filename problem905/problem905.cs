public class Solution {
    public int RepeatedNTimes(int[] A) {
        var intList = new List<int>();
        int res = 0;

        foreach (int a in A){
            if (intList.IndexOf(a)>=0){
                res = a;
                break;
            } else {
                intList.Add(a);
            }
        }

        return res;
    }
}