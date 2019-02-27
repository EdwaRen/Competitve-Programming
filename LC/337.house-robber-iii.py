# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        res = self.rob_recurse(root)
        return max(res[0], res[1])    
            
    def rob_recurse(self, node):
        if not node:
            return [0, 0]
        left = self.rob_recurse(node.left)
        right = self.rob_recurse(node.right)
        res = [0, 0]
        res[0] = node.val + left[1] + right[1]
        res[1] = max(left[0], left[1]) + max(right[0], right[1])
        return res

z = Solution()
a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(z.rob(None))
