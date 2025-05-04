class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        if len(s)<3:
            return []

        result=list()

        i=0
        while i<len(s)-2:
            if s[i]==s[i+1]==s[i+2]:
                first=i
                while i<=len(s)-2:
                    if s[i]==s[i+1]:
                        i+=1
                    else:                       
                        break
                second=i
                result.append([first,second])
            else:
                i=i+1

        return result 
            
