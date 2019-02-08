# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        pre = ListNode(0)
        pre.next = head
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
#        print("before merge", head.val, slow.val)
        return self.merge(l1, l2)


    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        #pre = ListNode(0)
        if l1.val > l2.val:
            l1, l2 = l2, l1

        pre = head = l1
        l1 = l1.next
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        
        if l1:
            pre.next = l1
            return head
        if l2:
            pre.next = l2
            return head
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
