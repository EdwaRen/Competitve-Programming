# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        # Find kth smallest element recursively
        cur = root

        # Succ defaults to None if nothing was found
        succ = None

        while cur and p:
            # Keep setting succ to be the largest element so far, otherwise go to the next largest
            if cur.val > p.val:
                succ = cur
                cur = cur.left

            # Try larger branch
            elif cur.val <= p.val:
                cur = cur.right
        
        return succ


z = Solution()

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

b.left = a
c.left = b
print(z.inorderSuccessor(c, a).val)

