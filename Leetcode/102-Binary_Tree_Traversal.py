import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, node):
        if not node:
            return []
        q = collections.deque([(node, 0)])
        res = []
        while q:
            p = q.popleft()
            cur, index = p[0], p[1]

            if cur.left:
                q.append((cur.left, index+1))
            if cur.right:
                q.append((cur.right, index+1))
            if index >= len(res):
                res.append([cur.val])
            else:
                res[index].append(cur.val)
        return res


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
# e.right = f
# f.left = g

print(s.levelOrder(None))
