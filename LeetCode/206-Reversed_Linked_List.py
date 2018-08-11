# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        while cur != None:
            print("cur info", cur.val)
            next_cur = cur.next
            cur.next = prev
            prev = cur
            cur = next_cur
        return prev

    def reverseList_recurse(self, head):
        if head != None:
            return self.recurse(head, [])
        return head

    def recurse(self, node, list):
        a = ListNode(node.val)
        list.append(node.val)
        if node.next != None:
            a.next = self.recurse(node.next, list)
        a.val = list.pop(0)
        return a

s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

r = s.reverseList(a)
print(r.val)
print(r.next.val)
