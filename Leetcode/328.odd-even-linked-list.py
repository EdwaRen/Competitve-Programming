# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        # Handle edge case
        if not head or not head.next:
            return head

        # Set odd and even pointers
        odd = head
        even = head.next
        
        # Keep track of even starting pointer
        even_start = even

        # Iterate through linkedlist, updating new pointers along the way
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            if odd is not None:
                even.next = odd.next
                even = even.next

        # Connect end of odd pointer to start of even pointer
        odd.next = even_start
        return head

    def printNode(self, head):
        # Helper function to print a linkedList
        while head:
            print (head.val)
            head = head.next

z = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
res = z.oddEvenList(None)
z.printNode(res)
