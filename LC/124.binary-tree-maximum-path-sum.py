# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        node_sum = 0

class Solution(object):
    def maxPathSum(self, root):

        def recurse(cur):
            if not cur:
                return 0
            r = recurse(cur.right)
            l = recurse(cur.left)
            self.max = max(self.max, cur.val + l + r)
            return max(cur.val, cur.val + max(l, r), 0)

        self.max = root.val
        recurse(root)
        return self.max

z = Solution()

a = TreeNode(12)
b = TreeNode(-15)
c = TreeNode(20)
d = TreeNode(15)
# d.val = -35
e = TreeNode(7)
# e.val = -7

a.left = b
a.right = c

c.left = d
c.right = e

f = TreeNode(0)

print(z.maxPathSum(c))