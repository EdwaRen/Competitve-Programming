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

        # Check edge case
        if not head:
            return None 
        
        # Set cur to be head
        cur = head

        # CHeck that cur is valid and it is not the tail
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next 
        return head 

z = Solution()
a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)

a.next = b 
b.next = c 
c.next = d
d.next = e  
e.next = f  

res = z.deleteDuplicates(a)
while a:
    print a.val
    a = a.next


