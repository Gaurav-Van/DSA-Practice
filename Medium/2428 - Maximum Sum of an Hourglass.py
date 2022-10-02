class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = []
        for a in range(len(grid)-2):
            for b in range(len(grid[0])-2):
                ans = (grid[a][b] + grid[a][b+1] + grid[a][b+2]) + grid[a+1][b+1] + (grid[a+2][b] + grid[a+2][b+1] + grid[a+2][b+2])
                result.append(ans)
        return max(result)
                
