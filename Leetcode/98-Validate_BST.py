# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inOrderTraverse(self, root):
        if root == None:
            return true
        stack = []
        prev = None
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if (prev != None and root != None and root.val <= prev.val):
                return False
            prev = root
            root = root.right
        return True


    def isValidBST(self, root):
        return self.inOrderTraverse(root)


a = TreeNode(4)
b = TreeNode(1)
c = TreeNode(6)
d = TreeNode(5)
e = TreeNode(11)
f = TreeNode(2)
a.left = b
a.right = c
c.left = d
c.right = e
e.left = f

s = Solution()
p = s.isValidBST(a)
print(p)
