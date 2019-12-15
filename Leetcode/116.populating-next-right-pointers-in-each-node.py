
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):

    def connect(self, root):
        # Iterative solution for true O(1)

        cur = None
        pre= root

        # Outer loop goes to the leftmost of the tree each time
        while pre and pre.left:
            # Set cur to the leftmost node
            cur = pre

            # This inner loop goes through each element of the current level and assigns the next function.
            # We setup the "bridges" with the important line: cur.right.next = cur.next.left
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left

        return root



    def connect_recruse(self, root):
        
        def recurse(node, ref):
            """
            This recursive solution works by keeping track of a reference tree at every left split. Where
            this split is passed onto the node's children so that we can track the Node.next when we recurse deeper at separate
            nodes
            """

            # Handle null case
            if not node:
                return 
            
            # Recurse, keeping None if necessary
            if ref:           
                recurse(node.right, ref.left)
            else:
                recurse(node.right, None)
            recurse(node.left, node.right)
           
            # Set node.next 
            node.next = ref    
            
        recurse(root, None)
        return root

    
    def print_tree(self, root, depth, margin):
        # Helper function to print the tree
        if root is None:
            return            

        self.print_tree(root.left, depth+margin, margin)
        if root.next:
            print(" " * depth, root.val, " | ",  root.next.val)
        else:
            print(" " * depth, root.val, " | ", None)

        self.print_tree(root.right, depth+margin, margin)


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
m = Node(13)
n = Node(14)
o = Node(15)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

d.left = h
d.right = i
e.left = j
e.right = k
f.left = l
f.right = m
g.left = n
g.right = o

new_a = z.connect(a)
z.print_tree(new_a, 0, 6)
