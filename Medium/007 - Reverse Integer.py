import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = list(str(x))
            x[:] = x[::-1]
            x = ''.join(x)
            x = int(x)
        else:
            x=abs(x)
            x = list(str(x))
            x[:] = x[::-1]
            x.insert(0, '-')
            x = ''.join(x)
            x = int(x)
            
        if x > int(math.pow(2, 31) - 1) or x < int(math.pow(-2, 31)):
            return 0
        else:
            return x
