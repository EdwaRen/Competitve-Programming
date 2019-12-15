# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(-1)
        dummy.next = head
        cur = head 
        pre = head
        
        while True:
            count = 0
            cur_count = cur
            while cur_count and count < k:
                count += 1
                cur_count = cur_count.next 

            if count == k:
 
                for i in range(k-1):
                    cur.next.next, cur.next, pre  = pre, cur.next.next, cur.next
 
                jump.next = pre
                jump = cur
                pre = cur.next
                cur = cur.next

                prntcur = cur
            else:
                return dummy.next

z = Solution()
a = ListNode(1)
b = ListNode(2)
a.next = b 
c = ListNode(3)
b.next = c 
d = ListNode(4) 
c.next = d 
e = ListNode(5)  
d.next = e  
y = z.reverseKGroup(a, 3)
while y:
    print(y.val)
    y = y.next                    
