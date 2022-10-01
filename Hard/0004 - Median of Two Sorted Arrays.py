class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1+nums2
        res.sort()
        if len(res) % 2 != 0:
            return float(res[((len(res) + 1)/2) - 1])
        else:
            n2 = res[(len(res)/2) - 1]
            n21 = res[len(res)/2]
            return float(float(n2 + n21)/2)
