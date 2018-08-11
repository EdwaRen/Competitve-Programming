# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        i = j = head
        labels = dict()
        while i:
            labels[i] = RandomListNode(i.label)
            i = i.next
        while j:
            labels[j].next = labels.get(j.next)
            labels[j].random = labels.get(j.random)
            j = j.next
        return labels.get(head)
a = Solution()
b = RandomListNode(1)
c = RandomListNode(2)
b.next = c
c.random = b
print(b.label)
print(b.next.label)
c = (a.copyRandomList(b))
b.label = 3
print("c new", c.label)
print(a.copyRandomList(b).next.label)
