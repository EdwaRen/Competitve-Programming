# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):

        # Handle edge case
        if not head or not head.next:
            return head

        # Pre is used to separate first and second half 
        pre = ListNode(0)
        pre.next = head
        slow = head
        fast = head

        # Divides linkedlist in half
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        # sorts first and second half recursively
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # Merges both halves of the original list
        return self.merge(l1, l2)


    def merge(self, l1, l2):

        # Handle edge case
        if not l1 or not l2:
            return l1 or l2

        # Ensures l1 starts with the smaller initial value
        if l1.val > l2.val:
            l1, l2 = l2, l1

        # Head keeps track of start, l1 is forwarded to l1.next since it's guaranteed to be the smaller value
        pre = head = l1
        l1 = l1.next

        # Merges both individually sorted lsits
        while l1 and l2:
            
            # pre variable changes according to the smallest .val
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        
        # Connects the end of the list depending on which hit None first
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2

        return head        
        
z = Solution()
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)

a.next = b
b.next = c
c.next = d


res = z.sortList(a)
while res:
    print(res.val, res.next)
    res = res.next
