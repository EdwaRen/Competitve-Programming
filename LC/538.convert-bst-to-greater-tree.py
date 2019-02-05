# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.children_sum = 0
        self.greater_sum = 0

class Solution(object):
    def convertBST(self, root):
        # self.recurse(root, 0)
        stack = []
        self.total = 0
        self.stack_solution(root)
        return root

    def recurse(self, node):
        if not node:
            return
        self.recurse(node.right)
        self.total += node.val
        node.val = self.total
        self.recurse(node.left)

    def stack_solution(self, root):
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            self.total += node.val
            node.val = self.total
            node = node.left
        return root



    # def recurse(self, node, parent_sum):
    #     if not node:
    #         return 0
    #     node.val += parent_sum
    #     if node.right:
    #         self.recurse(node.right, parent_sum)
    #         node.val += node.right.children_sum
    #         node.children_sum = node.right.children_sum
    #     node.children_sum += node.val
    #     parent_sum += node.children_sum
    #     if node.left:
    #         self.recurse(node.left, parent_sum)
    #         node.children_sum += node.left.children_sum

    def print_tree(self, node, index):
        if not node:
            return
        if node.right:
            self.print_tree(node.left, index+1)

        print( (index*" ") + str(node.val))

        if node.left:
            self.print_tree(node.right, index+1)

        
z = Solution()
a = TreeNode(13)
b = TreeNode(5)
c = TreeNode(18)
d = TreeNode(1)
e = TreeNode(8)
f = TreeNode(17)
g = TreeNode(21)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(z.convertBST(a))
z.print_tree(a, 0)
