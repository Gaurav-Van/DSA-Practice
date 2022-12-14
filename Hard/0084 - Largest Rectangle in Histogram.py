class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)

        left = [1] * n
        right = [1] * n
        max_rect = 0

        for i in range(0, n):
            j = i - 1
            
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: 
                    break
                    
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break

        for i in range(0, n):
            max_rect = max(max_rect, heights[i] * (left[i] + right[i] - 1))

        return max_rect
