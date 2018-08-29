class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parents = {root:None}
        if p == root or q == root:
            return root
        while p not in parents or q not in parents:
            t = stack.pop()
            if t.left != None:
                parents[t.left] = t
                stack.append(t.left)
            if t.right != None:
                parents[t.right] = t
                stack.append(t.right)
        history = set()
        while q != None:
            history.add(q)
            q = parents[q]
        while p not in history:
            p = parents[p]
        return p

s = Solution()
a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(7)
g = TreeNode(4)
h = TreeNode(0)
i = TreeNode(8)
a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# e.right = g
# c.left = h
# c.right = i
print(s.lowestCommonAncestor(a, b, a).val)
