# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import pprint
from queue import PriorityQueue

class Solution(object):
    def printList(self, list):
        while list:
            print(list.val)

    def mergeKLists(self, lists):
        p_queue = PriorityQueue()
        for h in lists:
            if h:
                print(h.val, h)
                p_queue.put((h.val, h.next))
        print("p quere done")
        head = cur = ListNode(-1)
        while not p_queue.empty():
            p = p_queue.get()
            print(p)
            val = p[0]
            node = p[1]
            cur.next = node
            node = node.next
            if node:
                p_queue.put(node.val, node)
        self.printList(head)

a = Solution()
b = ListNode(1)
b.next = ListNode(4)
b.next.next = ListNode(5)
c = ListNode(1)
c.next = ListNode(3)
c.next.next = ListNode(4)
d = ListNode(2)
d.next = ListNode(6)
a.mergeKLists([b, c, d])
