# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # Catch edge case
        if not head:
            return None 

        # Find mid
        rabbit, turtle = head.next, head
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next 
            turtle = turtle.next 

        # Reverse linkedlist starting at rabbit
        prev = None 
        nxt = None
        cur = turtle.next
        while cur:
            nxt = cur.next
            cur.next = prev 
            prev = cur 
            cur = nxt 
        
        turtle.next = None

        # Merge two linkedlists
        cur = head 
        while prev:
            tmp_cur, tmp_turt = cur.next, prev.next
            cur.next, prev.next = prev, cur.next
            prev = tmp_turt
            cur = tmp_cur

        return head 
            




z = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
# a.next = b 
# b.next = c 
# c.next = d   
# d.next = e
res = z.reorderList(a)

while res:
    print(res.val)
    res = res.next

        
