class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrderRecurse(self, node):

        if node == None:
            return [[]]

        def concat(l, r):
            new = []
            for i in range(max(len(l), len(r))):
                if i < len(l) and i < len(r):
                    new.append(l[i]+r[i])
                elif i < len(l):
                    new.append(l[i])
                elif i < len(r):
                    new.append(r[i])
            return new
        left = self.levelOrderRecurse(node.left)
        right = self.levelOrderRecurse(node.right)
        new = concat(left, right)
        res = [[node.val]] +new
        #print("res of ", node.val, res)
        #print("new", left)
        return res

    def levelOrder(self, node):
        res = self.levelOrderRecurse(node)
        return res[:-1]

s = Solution()
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
f = TreeNode(2)
g = TreeNode(1)
a.left = b
b.left = TreeNode(4)
a.right = c
c.left = d
c.right = e
e.right = f
f.left = g

print(s.levelOrder(a))
