class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()
        k = len(nums3)
        if k%2 ==1:
            mid = k//2
            return nums3[mid]
        else:
            return (nums3[(k//2)-1]+nums3[k//2])/2