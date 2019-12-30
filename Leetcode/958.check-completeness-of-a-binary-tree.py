# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Level order traversal until we reach a leaf in the queue
        q = [root]
        while q[0] != None:
            cur = q.pop(0)
            q.append(cur.left)
            q.append(cur.right)
        
        # If there is a valid node in the queue, the tree is incomplete
        # The queue stil contains all the remaining nodes in the level with the first None
        while q != []:
            if q.pop(0) != None:
                return False 
        return True

z = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
i = TreeNode(8)

a.left = b 
a.right = c  
b.left = d   
# b.right = e 
# c.left = f  
# c.right = g 
# d.right = i

print(z.isCompleteTree(a))
        
