# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        cur = res
        while l1 and l2:
            if l1.val > l2.val:
                c = ListNode(l2.val)
                cur.next = c
                cur = cur.next
                l2 = l2.next
            else:
                c = ListNode(l1.val)
                cur.next = c
                cur = cur.next
                l1 = l1.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return res.next

a = Solution()
b = ListNode(1)
c = ListNode(2)
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(5)
d.next = e
e.next = f

z = a.mergeTwoLists(b, d)
while z:
    print("z iter", z.val)
    z = z.next
