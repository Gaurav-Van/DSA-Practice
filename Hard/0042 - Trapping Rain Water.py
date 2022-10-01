class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trapwater = 0
        lm = height[0]
        rm = height[-1]
        l = 0
        r = len(height) - 1
        while l <= r:
            
            if height[l] <= height[r]:
                lm = max(lm, height[l]) 
                trapwater = trapwater + lm - height[l] 
                l = l+1
            
            else:
                rm = max(rm, height[r]) 
                trapwater = trapwater + rm -  height[r]
                r = r-1
            
        return trapwater
