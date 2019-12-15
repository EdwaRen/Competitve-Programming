# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA = headA
        curB = headB
        if headA == headB:
            return headA
        while curA != None and curB != None:
            curA = curA.next
            curB = curB.next
            if curA == None and curB == None:
                return None
            if curA == None:
                curA = headB
            if curB == None:
                curB = headA
            if curA == curB:
                return curA
        return None

s = Solution()
a1 = ListNode(11)
a2 = ListNode(12)
a3 = ListNode(13)
b1 = ListNode(21)
b2 = ListNode(22)
b3 = ListNode(23)
c1 = ListNode(31)
c2 = ListNode(32)
c3 = ListNode(33)
a1.next = a2
a2.next = a3
a3.next = c1
c1.next = c2
c2.next = c3
b1.next = b2
b2.next = b3
b3.next = c1
print(s.getIntersectionNode(c3, c3).val)
