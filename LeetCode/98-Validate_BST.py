# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recurse(self, node):
        if node == None:
            return (None, None)


        small = self.recurse(node.left)

        

        big = self.recurse(node.right)
        # if small[1] == False or big[1] == False:
        #     return (node.val, False)
        #
        # if small[1] == None and big[1] == None:
        #     return (node.val, True)
        # if small[1] != None and small[0] >= node.val:
        #     return (node.val, False)
        # if big[1] != None and big[0] <= node.val:
        #     return (node.val, False)
        # return (node.val, True)

    def isValidBST(self, root):
        return (self.recurse(root)[1] != False)


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(1)
e = TreeNode(1)
a.left = b
a.right = c
c.left = d
# c.right = e

s = Solution()
p = s.isValidBST(c)
print(p)
