class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        
        if n == 0:
            return True
        if m == 0:
            return False
        
        for a in s:
            if a not in t:
                return False
        
        while (i<n and j<m):
            
            if s[i] == t[j]:
                
                i = i+1
                
            j = j+1
        
        return i==n
