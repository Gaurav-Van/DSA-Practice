class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = []
        c = a
        d = b
        
        while(d):
            c, d = d, c%d
        check = c
        
        for i in range(1, check+1):
            if check%i == 0:
                ans.append(i)
        
        return len(ans)
