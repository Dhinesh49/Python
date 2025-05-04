class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
          return 0 
        count=1
        list1=[]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count+=1
            else:
                list1.append(count)
                count=1
        list1.append(count)
        return(max(list1))        
      
