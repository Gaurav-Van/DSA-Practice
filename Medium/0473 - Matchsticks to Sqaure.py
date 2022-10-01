class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        max_pos_side = perimeter // 4
        
        matchsticks.sort(reverse=True)
        
        sums = [0]*4
        
        def backtrack(cur):
            if cur == len(matchsticks): # last case
                return sums[0] == sums[1] == sums[2] == max_pos_side
            
            for i in range(4):
                if sums[i] + matchsticks[cur] <= max_pos_side:
                    sums[i] += matchsticks[cur]
                    if backtrack(cur+1):
                        return True
                    sums[i] -= matchsticks[cur]
            return False
        
        return backtrack(0)
