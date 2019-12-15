# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 1
        cur = head 
        pre = ListNode(-1)
        pre.next = head 

        # Orig and jump keep track of the first node
        # Jump gets modified on the first pass then forgotten about, but orig keeps the first node
        orig = jump = ListNode(-1)
        jump.next = head

        while cur and cur.next:
            # Swap m to nth element

            while count >= m and count < n and cur.next:
                # Swap elements iteratively
                pre.next, cur.next.next, cur.next = cur.next, pre.next, cur.next.next
                count += 1

            # Preserve the updated head node if the first element needs to be swapped
            jump.next = pre.next 
            jump = ListNode(-2)

            if count >= n:
                return orig.next

            # Update pre and cur for next iteration
            pre = cur
            cur = cur.next
            count += 1

        return orig.next

z = Solution()

a = ListNode(1)
b = ListNode(2)
a.next = b 
c = ListNode(3)
b.next = c  
d = ListNode(4)
c.next = d  
e = ListNode(5) 
d.next = e 

res = z.reverseBetween(a, 3, 5)
while res:
    print(res.val) 
    res = res.next 