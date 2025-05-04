class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left,right+1):
            num = i
            flag = False
            while num > 0:
                remainder = num % 10
                num = num // 10
                if remainder == 0 or i % remainder != 0:
                    flag = False
                    break
                elif i % remainder == 0:
                    flag = True
            if flag == True:
                ans.append(i)
        return ans
        
