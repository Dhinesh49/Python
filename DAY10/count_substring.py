class Solution(object):
    def countBinarySubstrings(self, s):
        count = 1
        g = []
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else :
                g.append(count)
                count = 1
        g.append(count)
        for i in range(1, len(g)):
            result += min(g[i], g[i-1])
        return result
        
