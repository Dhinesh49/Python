class Solution:
    def __init__(self):
        self.Inorder = []
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.Inorder.append(root.val)
        self.inorder(root.right)
    
    def minDiffInBST(self, root):
        if not root:
            return 0
        self.inorder(root)
        res = float('inf')
        for i in range(1, len(self.Inorder)):
            res = min(res, self.Inorder[i] - self.Inorder[i-1])
        return res
