# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        serial = ['']
        def recurse(node):
            if node == None:
                serial[0]+=("% ")
            else:
                serial[0]+=str(node.val) + " "
                recurse(node.left)
                recurse(node.right)
        recurse(root)
        return serial[0]

    def deserialize(self, data):
        input = data.split(' ')
        def recurse():
            val = input.pop(0)
            if val == '%':
                return None
            cur = TreeNode(val)
            cur.left = recurse()
            cur.right = recurse()
            return cur
        return recurse()

s = Codec()
One  = TreeNode(1)
Two = TreeNode(2)
Three = TreeNode(3)
Four = TreeNode(4)
Five = TreeNode(5)
One.left = Two
One.right = Three
Three.left = Four
Three.right = Five

r = (s.deserialize(s.serialize(One)))
print (r.val)
print(r.left.val)
print(r.right.val)
print(r.right.left.val)
print(r.right.right.val)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
