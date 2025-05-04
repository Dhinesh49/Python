class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        s=bin(n)[2:]
        k,m=0,0
        for i in range(1,len(s)):
            if s[i]=='1':
                m=max(m,i-k)
                k=i
            

        return m
        
        
