class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!= len(goal):
            return False
        if s==goal:
            for i in s:
                if s.count(i)>=2:
                    return True
                      
        result=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                result.append(i)

        if len(result)!=2:
            return False
        goal=list(goal)
        goal[result[0]],goal[result[1]]=goal[result[1]],goal[result[0]]
        goal=''.join(goal)

        return s==goal
