# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):

        # Base case
        if not head or not head.next:
            return head 

        # Swap recursively
        tmp = head.next 
        head.next = self.swapPairs(head.next.next)
        tmp.next = head 

        return tmp


    def swapPairsLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Use a dummy node to keep track of the previous 
        dummy = ListNode(-1)
        dummy.next = head 

        # Keep track of the first node
        hold = dummy

        # Look while possible
        while dummy.next and dummy.next.next:
            next1 = dummy.next 
            next2 = dummy.next.next 
            next3 = dummy.next.next.next 

            next2.next = next1
            next1.next = next3
            dummy.next = next2

            dummy = next1


        return hold.next

z = Solution()
a = ListNode(1)
b = ListNode(2)
a.next = b 
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d  
# e = ListNode(5)
# d.next = e

res = z.swapPairs(a)

while res:
    print(res.val)
    res = res.next