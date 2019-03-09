# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.iterate(root)
   
    def iterate(self, root):
        # Initializes both sides of the tree
        stack = [[root.left, root.right]]

        # Continue iterating as long as the stack is valid
        while stack:
            
            # Pop off the most current element of the stack and perform checks
            cur = stack.pop()

            if cur[0] == None and cur[1] == None:
                # Thank you, next
                continue
            elif cur[0] == None or cur[1] == None:
                return False
            elif cur[0].val != cur[1].val:
                return False

            # Insert next stack elements
            stack.append([cur[0].left, cur[1].right])
            stack.append([cur[0].right, cur[1].left])

        # Not false, must be true
        return True

 
    def recurse(self, r1, r2):
        # Conditions for recursive traverse        
        if r1 == None and r2 == None:
            return True
        elif r1 == None or r2 == None:
            return False
        elif r1.val != r2.val:
            return False

        # Both left and right recurse must return true
        return self.recurse(r1.left, r2.right) and self.recurse(r1.right, r2.left)
        
z = Solution()
a = TreeNode(1)
b = TreeNode(2)
b2 = TreeNode(2)
c = TreeNode(3)
c2 = TreeNode(3)

a.left = b
a.right = b2
b.left = c
b2.left = c2

print(z.isSymmetric(a))





        
