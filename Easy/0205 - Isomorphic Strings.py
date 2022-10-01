class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dic = {}
        se = set()
        
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            
            if x in dic:
                
                if dic[x] != y:
                    return False
            
            else:
                
                if y in se:
                    return False
                
                dic[x] = y
                se.add(y)
                
        return True
