# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        # Handle edge case
        if not root:
            return 0

        # Set global max
        self.max_len = 0
        self.recurse(root)
        return self.max_len -1

    def recurse(self, root):
        if not root:
            return 0
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        print(root)
        print(root.val)
        if left+right +1 > self.max_len:
            self.max_len = left+right+1
        root.val = max(left, right) + 1
        return root.val


# z = Solution()
# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# e.left = f
# print(z.diameterOfBinaryTree(a))
