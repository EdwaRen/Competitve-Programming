# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def init_stacks(self, l1, l2, s1, s2):
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

    def attachNode(self, next_sum, node):
        next_sum = next_sum % 10
        current_node = ListNode(next_sum)
        current_node.next = node
        return current_node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []

        self.init_stacks(l1, l2, s1, s2)

        carry = 0
        cur = None

        while s1 and s2:
            next_sum = s1.pop() + s2.pop() + carry
            carry = next_sum / 10
            cur = self.attachNode(next_sum, cur)

        while s1:
            next_sum = s1.pop() + carry
            carry = next_sum / 10
            cur = self.attachNode(next_sum, cur)

        while s2:
            next_sum = s2.pop() + carry
            carry = next_sum / 10
            cur = self.attachNode(next_sum, cur)

        if carry > 0:
            cur_next = ListNode(carry)
            cur_next.next = cur
            cur = cur_next

        return cur

z = Solution()
ls1 = ListNode(7)
ls2 = ListNode(2)
ls3 = ListNode(4)
ls4 = ListNode(3)
ls1.next = ls2
ls2.next = ls3
ls3.next = ls4

lt1 = ListNode(5)
lt2 = ListNode(6)
lt3 = ListNode(4)
lt1.next = lt2
lt2.next = lt3
# ls1 = ListNode(5)
# lt1 = ListNode(5)

res = z.addTwoNumbers(ls1, lt1)
print("RESULT: ")
while res:
    print(res.val)
    res = res.next
