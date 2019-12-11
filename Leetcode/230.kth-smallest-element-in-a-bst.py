# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def kthSmallest(self, root, k):
        cur = root
        
        count = 0
        stack = [root]

        # Iterative inorder traversal
        while stack or cur:
            
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            # Count and check if kth smallest
            count +=1
            if count == k:
                return cur.val

            # Go to right node
            cur = cur.right

        return None

    def kthSmallest_recurse(self, root, k):
        self.count = 0
        self.res = 0
        self.recurse(root, k)
        return self.res

    def recurse(self, node, k):
        if not node:
            return
 
        # Recurse with InOrder traversal
        self.recurse(node.left, k) 
        self.count +=1      
 
        # Count with global variable instead of returning
        if self.count == k:
            self.res = node.val

        self.recurse(node.right, k)

z = Solution()
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(4)
a.left = b
a.right = d
b.right = c

print(z.kthSmallest(a, 4))





