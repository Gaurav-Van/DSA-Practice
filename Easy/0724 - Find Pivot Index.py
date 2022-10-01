class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumL = 0
        sumR = 0
        for i in range(len(nums)):
            if i == 0:
                sumL = 0
            else:
                sumL =sumL + nums[i-1]
            
            sumR = sum(nums[i+1:])
            
            if sumL == sumR:
                return i
        
        return -1
