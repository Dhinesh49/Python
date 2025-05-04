
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class KthLargest(object):

#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """

#         self.k = k
#         self.root = None
#         #print("Input List:", nums)

#         for num in nums:
#             #print(f"Inserting {num} into BST")
#             self.root = self.insertBST( self.root, num)
#             #print("printing BST")
#             #print(self.inorderTraversal_iter(self.root))  # Print the BST after each insertion

    
#     def insertBST(self, root, val):
#         """ Insert a value into BST and return the updated root """

#         if root is None:
#             #print(f"Inserted {val} as root node")   
#             return TreeNode(val)

#         current = root
#         bst_travel = []

#         while current:
            
#             # if val == current.val:
#             #     print(f"Value {val} already exists in the BST. Insertion terminated.")
#             #     return root  # Terminate the insertion operation


#             bst_travel.append(current.val)
#             #print(f"Current Node: {current.val}")  # Debugging

#             if val <= current.val:
                
#                 if current.left is None:
#                     current.left = TreeNode(val)
#                     #print(f"Inserted {val} as left child of {current.val}")  # Debugging
#                     break
#                 current = current.left
#             else:
#                 if current.right is None:
#                     current.right = TreeNode(val)
#                     #print(f"Inserted {val} as right child of {current.val}")  # Debugging
#                     break
#                 current = current.right

#         #print("bst_travel:", bst_travel)
#         return root


    

    
#     def inorderTraversal_iter(self, root):
        
#         if root is None:
#             return []
        
        
#         res = []
#         stack = []
#         current = root
        
#         while stack or current :
            
#             # Step 1: Traverse left subtree
#             while current:
#                 stack.append(current)
#                 current=current.left
                
#             # Step 2:  pop out the left most and process it 
#             node = stack.pop()
#             res.append(node.val)
            
#             # Step 3: Move to the right subtree
#             current = node.right
                
#         return res

#     def kthLargestBST(self,root):
#         " implemented uisng reverse inorder "

#         stack = []
#         current = root
#         bst_traversal = []

#         count = 0
#         while current or stack :

#             while current:
#                 stack.append(current)
#                 current = current.right
            
#             current = stack.pop()
#             count +=1
#             if count == self.k:
#                 return current.val
                
#             current = current.left

        
#         return None  # If k is out of bounds

        



#     def add(self, val):
#         """
#         Add new element and return kth largest
#         :type val: int
#         :rtype: int
#         """

#         self.root = self.insertBST (self.root ,val )
#         #print("printing BST")
#         #print(self.inorderTraversal_iter(self.root))  # Print the BST after each insertion

#         res = self.kthLargestBST(self.root)
#         return res
      


# # Example Usage
# #obj = KthLargest(3, [4, 5, 8, 2])
# #print(obj.add(3))  # Should return the 3rd largest element
# #print(obj.add(10))  # Should update the BST and return new 3rd largest


    # BST
    # def __init__(self, k, nums):
    #     """
    #     :type k: int
    #     :type nums: List[int]
    #     """

    #     self.k = k
    #     self.stream = nums
    #     self.stream.sort()



    # def add(self, val):
    #     """
    #     Add new element and return kth largest
    #     :type val: int
    #     :rtype: int
    #     """

    #     index = self.get_index(val)
    #     self.stream.insert(index,val)
    #     return  self.stream[-self.k]


    # def get_index(self,val):

    #     left , right = 0, len(self.stream)-1

    #     while left <= right :

    #         middle = (left+right) //2

    #         if val == self.stream[middle] :
    #             return middle

    #         elif val > self.stream[middle] :
    #             left = middle + 1
            
    #         else:
    #             right = middle-1

        
    #     return left

    # Heap

        import heapq

        def __init__(self, k, nums):
            """
            :type k: int
            :type nums: List[int]
            """

            self.k = k
            self.min_heap = []
            for num in nums:
                self.add(num)
            



        def add(self, val):
            """
            Add new element and return kth largest
            :type val: int
            :rtype: int
            """

            if len(self.min_heap) < self.k :
                heapq.heappush(self.min_heap, val)

            else:
                if  val >  self .min_heap[0] :
                    heapq.heappush(self.min_heap, val)
                    if len(self.min_heap) > self.k :
                        heapq.heappop(self.min_heap)

            return self.min_heap[0]

            

            
