class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        
        import math
        while math.log10(num) >= 1:
            temp = list(str(num))
            temp = [int(i) for i in temp]
            num = sum(temp)
        return num
