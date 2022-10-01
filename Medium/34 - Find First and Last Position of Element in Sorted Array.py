class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lis_num = [i for i in range(len(nums)) if nums[i] == target]
        answer=[]
        if len(lis_num) != 0:
            answer.extend([lis_num[0], lis_num[-1]])
            return answer
        else:
            answer.extend([-1, -1])
            return answer
