"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def recurse(node):
            if node:
                # Pre order traversal
                recurse(node.left)

                if self.last:
                    self.last.right = node 
                    node.left = self.last 
                else:
                    self.first = node

                self.last = node 
                recurse(node.right)

        if root == None:
            return None


        self.last = None
        self.first = None

        recurse(root)

        self.first.left = self.last 
        self.last.right = self.first

        return self.first
        
z = Solution()
a = Node(4)
b = Node(2)
c = Node(5) 

a.left = b 
a.right = c  
d = Node(1) 
e = Node(3)
b.left = d 
b.right = e


k = Node(8)
i = Node(-6)
j = Node(-8)
k.left = i 
i.left = j

res = z.treeToDoublyList(b)
res_orig = res
while res:
    print(res.val)
    res = res.right 
    if res == res_orig:
        break

print(res_orig.left.val)
print(res.val)