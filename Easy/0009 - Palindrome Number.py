class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sample = list(str(x))
        res1 = sample[::-1]
        sample = ''.join(sample)
        res = ''.join(res1)
        if sample == res:
            return True
        else:
            return False
