
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        def isTree(a,b):

            if a==None and b==None:

                return True

            elif a==None or b==None:

                return False

            elif a.val!=b.val:

                return False


            return isTree(a.left,b.left) and isTree(a.right,b.right)

        def traversal(root):

            if root == None:

                return False

            
            if isTree(root,subRoot):

                return True

            return traversal(root.left) or traversal(root.right)

        return traversal(root)

            
        
