class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):

        def recurse(a1, a2):
            if a1 == None:
                return a2
            if a2 == None:
                return a1
            cur = TreeNode(a1.val + a2.val)
            cur.left = recurse(a1.left, a2.left)
            cur.right = recurse(a1.right, a2.right)
            return cur
        return recurse(t1, t2)

z = Solution()
a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(2)
d = TreeNode(5)
a.left = b
a.right = c
b.left = d

e = TreeNode(2)
f = TreeNode(1)
g = TreeNode(3)
h = TreeNode(4)
i = TreeNode(7)
e.left = f
e.right = g
f.right = h
g.right = i

res = (z.mergeTrees(a, e))
print(res.val)
print(res.left.val)
print(res.right.val)
print(res.left.left.val)
print(res.left.right.val)
print(res.right.right.val)
