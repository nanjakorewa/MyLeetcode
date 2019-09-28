class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        notInArr2 = []

        for i, ni in enumerate(arr1):
            if not ni in arr2:
                notInArr2.append(ni)
                arr1[i] = -1
            else:
                arr1[i] = arr2.index(ni)

        arr1.sort()
        notInArr2.sort()
        return [arr2[n] for n in arr1 if n>=0] + notInArr2
