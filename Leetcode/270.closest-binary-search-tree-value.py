# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        res = root.val

        cur = root
        while cur is not None:
            # Update possible res at every height
            if abs(cur.val - target) < abs(res - target):
                res = cur.val
            cur = cur.right if cur.val < target else cur.left

        return res 

z = Solution()
a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(3)
a.left = b 
a.right = c  
b.left = d   
b.right = e 

f = TreeNode(2)
g = TreeNode(0)
h = TreeNode(1)
f.left = g 
g.right = h

res = z.closestValue(f, 0.2)
print(res)
       
