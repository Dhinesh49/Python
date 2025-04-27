class Solution(object):
    def findMode(self, root):
        self.prev = None
        self.count = 0
        self.maxCount = 0
        self.res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is None or self.prev != node.val:
                self.count = 1
            else:
                self.count += 1

            if self.count > self.maxCount:
                self.maxCount = self.count
                self.res = [node.val]
            elif self.count == self.maxCount:
                self.res.append(node.val)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.res
