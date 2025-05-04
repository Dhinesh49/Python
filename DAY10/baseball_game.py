class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result=[]
        for i in range(len(operations)):
            if operations[i]=='+':
                a=int(result[-1])+int(result[-2])
                result.append(a)
            elif operations[i]=='D': 
                a=int(result[-1])*2
                result.append(a)
            elif operations[i]=='C': 

                result.pop()
            else:
                result.append(operations[i])
        sum=0
        for i in result:
            sum+=int(i)
        return sum               
