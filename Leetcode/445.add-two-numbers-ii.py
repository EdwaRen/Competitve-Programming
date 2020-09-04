# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        s1 = [l1.val]
        s2 = [l2.val]
        while l1.next:
            s1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            s2.append(l2.next.val)
            l2 = l2.next

        dig = s1.pop() + s2.pop()
        res = ListNode(dig, None)
        carry = int(math.floor(dig/10))
        while s1 and s2:
            dig = s1.pop() + s2.pop() + carry
            tmp = ListNode(dig%10, res)
            res = tmp
            carry = int(math.floor(dig/10))
        while s1:
            dig = s1.pop() + carry
            tmp = ListNode(dig%10, res)
            res = tmp
            carry = int(math.floor(dig/10))
        while s2:
            dig = s2.pop() + carry
            tmp = ListNode(dig %10, res)
            res = tmp
            carry = int(math.floor(dig/10))
        return res

z = Solution()
# ls1 = ListNode(7)
# ls2 = ListNode(2)
# ls3 = ListNode(4)
# ls4 = ListNode(3)
# ls1.next = ls2
# ls2.next = ls3
# ls3.next = ls4

# lt1 = ListNode(5)
# lt2 = ListNode(6)
# lt3 = ListNode(4)
# lt1.next = lt2
# lt2.next = lt3
ls1 = ListNode(5)
lt1 = ListNode(5)

res = z.addTwoNumbers(ls1, lt1)
while res:
    print(res.val)
    res = res.next
