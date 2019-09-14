class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # リストをソート
        nums1_nums2 = nums1 + nums2
        nums1_nums2.sort()
        med_index = len(nums1_nums2)/2
        
        # 長さが偶数奇数で場合分け
        if med_index.is_integer():
            return (nums1_nums2[int(med_index-.5)]+nums1_nums2[int(med_index+.5)])/2.0
        else:
            return nums1_nums2[int(med_index)]