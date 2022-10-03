class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        left_direction_window = 0
        result = 0
        
        for right_direction_window in range(len(s)):
            
            while s[right_direction_window] in hashset:
                hashset.remove(s[left_direction_window])
                left_direction_window = left_direction_window + 1
                
            hashset.add(s[right_direction_window])
            result = max(result, right_direction_window-left_direction_window+1)
        
        return result
            
