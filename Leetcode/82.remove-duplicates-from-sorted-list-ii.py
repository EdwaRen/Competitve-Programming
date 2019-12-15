# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Define dummy node to keep track of start even if the first node needs to be 
        # removed
        dummy = ListNode(-1) 
        dummy.next = head
        pre = dummy 
        cur = head

        while cur:
            # Remove duplicates
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur.next = cur.next.next 
                pre.next = cur.next
                
            # Only advance pre when no duplicates are detected
            else:
                pre = pre.next 
            cur = cur.next 
         
        return dummy.next

z = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
# d = ListNode(3)
# e = ListNode(3)
# f = ListNode(5)

a.next = b 
b.next = c 
# c.next = d
# d.next = e  
# e.next = f  

res = z.deleteDuplicates(a)
while res:
    print res.val
    res = res.next