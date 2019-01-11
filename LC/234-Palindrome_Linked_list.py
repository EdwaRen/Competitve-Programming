# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if head == None:
            return True
        cur = head
        runner = head.next
        temp = None
        odd = True
        while cur != None and runner != None:
            cur2 = cur
            cur = cur.next
            cur2.next = temp
            temp = cur2
            if runner.next != None:
                runner = runner.next.next
            else:
                odd = False
                runner = None
        if odd == True:
            cur = cur.next
        while temp != None and cur != None:
            if temp.val != cur.val:
                return False
            temp = temp.next
            cur = cur.next
        return True

s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
d2 = ListNode(5)

e = ListNode(4)
f = ListNode(3)
g = ListNode(2)
h = ListNode(2)
a = None
# a.next = None
b.next = None
c.next = d
d.next = d2
d2.next = e
e.next = f
f.next = g
g.next = h
print(s.isPalindrome(a))
