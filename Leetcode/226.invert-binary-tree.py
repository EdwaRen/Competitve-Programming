# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def invertTree(self, root):
        stack = [root]

        # Iterate while stack is full
        while stack:

            # pop most recent node
            cur = stack.pop()

            # Node must be valid
            if cur:

                # Swap left and right
                cur.left, cur.right = cur.right, cur.left

                # Append next nodes to stck
                stack.append(cur.left)
                stack.append(cur.right)

        return root

    def invertTreeRecurse(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTreeRecurse(root.right), self.invertTreeRecurse(root.left)

        return root

    def binaryPrint(self, cur, d):
        ret = ""
        if not cur:
            return

        if cur.right != None:
            ret += self.binaryPrint(cur.right, d + 4)

        ret += "\n" + (" " * d) + str(cur.val)

        if cur.left != None:
            ret += self.binaryPrint(cur.left, d + 4)

        return ret
        
z = Solution()

a = TreeNode(4)
b1 = TreeNode(7)
b2 = TreeNode(2)
c1 = TreeNode(9)
c2 = TreeNode(6)
c3 = TreeNode(3)
c4 = TreeNode(1)

a.left = b1
a.right = b2

b1.left = c1
b1.right = c2

b2.left = c3
b2.right = c4

# inv = z.invertTree(a)
# print(z.binaryPrint(inv, 4))
print("------")
print(z.binaryPrint(a, 4))
