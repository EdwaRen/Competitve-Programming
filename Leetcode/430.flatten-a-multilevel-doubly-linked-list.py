"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        # Handle edge case 
        if not head:
            return None 
        self.flatten_rec(head)
        return head

    def flatten_rec(self, head):
        cur, prev = head, head

        while cur:
            
            # Branch off and update cur.next to be the end of the child branch
            if cur.child:
                # Useful variables holding node pointers
                child_branch_end = self.flatten_rec(cur.child)
                cur_next = cur.next 

                # Relink nodes
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
                child_branch_end.next = cur_next

                if cur_next:
                    cur_next.prev = child_branch_end
                cur = cur_next
                prev = child_branch_end
            else:
                prev = cur
                cur = cur.next

        # Always return a valid node
        return prev 



    def flatten_iter(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head 

        # Keep track of all branching nodes with a stack
        stack = [head]
        pre = Node(-1)
        pre.next = head

        cur = head

        while stack:
            # Since stack only contains branches, we MUST link pre to the newly popped branch
            cur = stack.pop()
            pre.next = cur
            cur.prev = pre

            pre = cur
            # Skip singly linked nodes until we find a branch of an end
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                # Set pre, the state of the list before branching off
                # pre gets updated as we go to always be the last node before the next pop
                stack.append(cur.child)
                cur.child = None


        head.prev = None
        return head

    

    

z = Solution()
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6) 
g = Node(7) 
h = Node(8)
i = Node(9)
j = Node(10)
k = Node(11)
l = Node(12)

a.next = b 
b.next = c  
b.prev = a 
c.next = d  
c.prev = b 
c.child = g  
d.next = e 
d.prev = c  
e.next = f 
e.prev = d   
f.prev = e

g.next = h 
h.next = i 
h.prev = g 
h.child = k 
i.next = j 
i.prev = h 
j.prev = i 
k.next = l 
k.prev = h 
l.prev = k

(z.flatten(a))
res = a
while res:
    print(res.val)
    res = res.next