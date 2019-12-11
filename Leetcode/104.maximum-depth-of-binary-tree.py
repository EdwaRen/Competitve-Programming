# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):

        # Initialization
        stack = [[root, 1]]
        if not root:
            return 0
        cur = root
        res = 0
        depth = 1

        # Tree is fully iterated when the stack is empty
        while stack:

            # Performs an inorder traversal iteratively
            while cur:
                stack.append([cur, depth])
                cur = cur.left
                depth+=1

            # Update current node and depth
            cur_pop = stack.pop()
            cur = cur_pop[0]
            depth = cur_pop[1]

            # Update max depth
            res = max(res, depth)
            cur = cur.right     
            depth+=1

        return res           

    
    def maxDepthRecurse(self, root):
        # Trivial recursive approach
        if not root:
            return 0
        return max(self.maxDepthRecurse(root.left), self.maxDepthRecurse(root.right)) + 1

z = Solution()

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.right = d
d.left = e
print(z.maxDepth(a))





        
