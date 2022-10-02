# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lis = []
        temp = head
        while(temp!=None):
            lis.append(temp.val)
            temp = temp.next
            
        temp = head
        lis.sort()
        i = 0
        
        while(temp!=None) or i < len(lis):
            temp.val = lis[i]
            temp = temp.next
            i = i+1 
        
        return head
