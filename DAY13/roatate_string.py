class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)
        for i in range(n):
            tmp = s[i:n] + s[0:i]
            if tmp == goal:
                return True
        return False
        
