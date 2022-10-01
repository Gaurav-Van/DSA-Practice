class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) > 2:
                while nums.count(i) > 2:
                    nums.remove(i)
        
        return len(nums)
