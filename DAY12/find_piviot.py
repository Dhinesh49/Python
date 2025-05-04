class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # construct two list (left_sum, right_sum) to record the sum of each index
        left_sum, right_sum = 0, sum(nums[1:])

        # loop for nums
        for index in range(len(nums)):
            # check whether the left and right are equal
            if left_sum == right_sum:
                return index
            # update the list
            left_sum += nums[index]
            if index < len(nums)-1:
                right_sum -= nums[index+1]

        return -1



        
