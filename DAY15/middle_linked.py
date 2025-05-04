# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def get_length(l):
            count = 0
            while l!=None:
                l = l.next
                count+=1
            return count
        count = get_length(head)//2
        while head!=None and count!=0:
            head = head.next
            count-=1
        return head
