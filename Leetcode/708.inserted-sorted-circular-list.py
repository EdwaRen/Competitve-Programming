# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # This question is mostly about how to handle edge cases

        # Handle empty case
        if not head:
            res = Node(insertVal)
            res.next = res 
            return res

        prev = head
        cur = head.next

        def insert_between(prev, cur, insertVal):
            prev.next = Node(insertVal, cur) 

        while cur != head:
            # insertVal is between two sorted nodes
            if (insertVal >= prev.val and insertVal < cur.val) or (insertVal > prev.val and insertVal <= cur.val):
                insert_between(prev, cur, insertVal)
                return head
            
            # insertVal is bigger than both start and end nodes
            if cur.val < prev.val and insertVal >= cur.val and insertVal >= prev.val:
                insert_between(prev, cur, insertVal)
                return head

            # insertVal is smaller than both start and end nodes
            if cur.val < prev.val and insertVal <= cur.val and insertVal <= prev.val:
                insert_between(prev, cur, insertVal)
                return head

            prev = cur 
            cur = cur.next

        # Handle edge case of all same values
        insert_between(prev, cur, insertVal)
        return head 

z = Solution()
a = Node(4)
b = Node(5)
c = Node(1)
d = Node(2)

a.next = b 
b.next = c  
c.next = d   
d.next = a 

res = z.insert(a, 3)

cur = res.next
print(res.val)

while cur != res:
    print(cur.val)
    cur = cur.next
print("RELINK")
print(cur.val)