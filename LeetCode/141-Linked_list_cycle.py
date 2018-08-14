# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            walker = head
            runner = head.next
            while walker is not  runner:
                walker = walker.next
                runner = runner.next.next
            return True
        except:
             return False
s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = a

print(s.hasCycle(a))
