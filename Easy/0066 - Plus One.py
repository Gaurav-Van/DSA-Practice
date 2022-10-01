class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[:] = [str(i) for i in digits]
        digits[:] = list(str(int(''.join(digits)) + 1))
        digits[:] = [int(i) for i in digits]
        return digits
