class Solution(object):
    def hammingDistance(self, x, y):
        xor = x^y
        c = 0
        while xor:
            c+= xor%2
            xor //= 2
        return c
