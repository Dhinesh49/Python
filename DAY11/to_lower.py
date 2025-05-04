class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in s:
            if i >= 'A' and i<='Z':ans += chr(ord(i)+32)
            else: ans += i
        return ans
        
