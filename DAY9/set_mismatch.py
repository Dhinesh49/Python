class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        # Expected sum and sum of squares of 1 to n
        sum_n = (n * (n + 1)) // 2
        sum_n_square = (n * (n + 1) * (2 * n + 1)) // 6

        # Actual sum and sum of squares from array
        sum_nums = sum(nums)
        sum_nums_square = sum(x * x for x in nums)

        # Equations: x - y = diff, x + y = diff2 / diff
        diff = sum_n - sum_nums                 # (x - y)
        diff2 = sum_n_square - sum_nums_square # (x^2 - y^2)

        missing_plus_duplicate = diff2 // diff # (x + y)

        # Solve for missing (x) and duplicate (y)
        missing = (diff + missing_plus_duplicate) // 2
        duplicate = missing_plus_duplicate - missing

        return [duplicate, missing]
