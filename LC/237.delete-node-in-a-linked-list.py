# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        # This question is ???
        node.val = node.next.val
        node.next = node.next.next       
        

z = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

z.deleteNode(b)
print(a.val)
print(a.next.val)

