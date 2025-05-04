# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        # Using mutable lists to behave global values within recursion
        # Setting to numbers that are unlikely to be used

        prev = [-999999]
        res = [999999]

        # Inorder traversal
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            # Ignores first time it is used so prev is always last value
            if prev[0] != -999999:
                # We used inorder traversal so this works as always 
                # calculating children value against the parents
                res[0] = min(abs(node.val - prev[0]), res[0])

            # Sets previous to last used value
            prev[0] = node.val

            dfs(node.right)

        # Calls function and returns where we stored the answer
        dfs(root)
        return res[0]
