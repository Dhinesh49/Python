class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums) - 1
        return max(nums[n]*nums[n-1]*nums[n-2],nums[0]*nums[1]*nums[n])

        
