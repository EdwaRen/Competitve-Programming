# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):

        def bfs_recurse(node):
            right = {}
            max_depth = -1
            q = deque([(root, 0)])
            while q:
                cur, depth = q.popleft()
                if cur:
                    max_depth = max(max_depth, depth)
                    right[depth] = cur.val
                    q.append((cur.left, depth+1))
                    q.append((cur.right, depth+1))
            res =  [right[depth] for depth in range(max_depth+1)]
            return res


        def dfs_recurse_old(node, level):
            if node:
                if level >= len(res):
                    res.append(node.val)
                dfs_recurse(node.right, level+1)
                dfs_recurse(node.left, level+1)

        return bfs_recurse(root)

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
e = TreeNode(4)
f = TreeNode(6)
a.left = b
a.right = c
b.right = d
# d.right = f
c.right = e

print(s.rightSideView(a))
