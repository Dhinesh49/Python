class Solution(object):
    def findTheDifference(self, s, t):
        res = 0
        for c in s + t:
            res ^= ord(c)
        return chr(res)
