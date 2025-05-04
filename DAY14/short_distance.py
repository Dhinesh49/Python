class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        ans = [float('inf')] * n
        index = -1

        # Left to right
        for i in range(n):
            if s[i] == c:
                index = i
            if index != -1:
                ans[i] = i - index

        # Right to left
        for i in range(index - 1, -1, -1):
            if s[i] == c:
                index = i
            ans[i] = min(ans[i], index - i)

        return ans
        
