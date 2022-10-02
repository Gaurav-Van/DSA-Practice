class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        ans = 0
        
        while(i<j):
            
            stored = min(height[i], height[j])*(j-i) #Water will be stored on the basis of shortest bar - Point 1
            ans = max(ans, stored)
            
            if(height[i]<height[j]): 
                #if left is already smallest then there is no point of decreasing right. Refer to Point 1 
                i = i+1
            else:
                #if right is already smallest then there is no point of increasing left. Refer to Point 1
                j = j-1
                
        return ans
