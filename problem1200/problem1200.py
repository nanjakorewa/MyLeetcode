class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        mindiff = 10**6
        for i in range(len(arr)-1):
            diff = abs(arr[i+1]-arr[i])
            if diff<mindiff:
                mindiff = diff
                res.clear()
                res.append([arr[i], arr[i+1]])
            elif diff==mindiff:
                res.append([arr[i], arr[i+1]])
        return res