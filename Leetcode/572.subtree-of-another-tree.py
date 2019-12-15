# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        # Handle edge case
        if t == None:
            return True
       
        # dfs basically flattens the tree into a string and we check if t is a substring of s 
        def dfs(root):

            # String ending with #
            if not root:
                return "#"

            # Recurse
            left = dfs(root.left)
            right = dfs(root.right)

            # Create unique string
            return "/" + str(root.val) + " " + left + " " + right + " "

        bigtree = dfs(s)
        smoltree = dfs(t)
        
        # check if smoltree is subtring of bigtree
        return smoltree in bigtree


    def isSubtreeRecurse(self, s, t):
        
        # Base case when only one tree ends
        if s == None or t == None:
            return False
        
        # Pattern match when the two tree values match
        elif s.val == t.val:
            
            # Recurse again if res is initially false
            res =  self.recurseFind(s, t)
            if not res:
                return self.isSubtreeRecurse(s.left, t) or self.isSubtreeRecurse(s.right, t)
            else:
                return True
        else:
            # Continue recursing through left and right of the tree, while t remains the same
            l = self.isSubtreeRecurse(s.left, t)
            r = self.isSubtreeRecurse(s.right, t)
            
            return l or r

    def recurseFind(self, t1, t2):
        # Base case, both tree branches match
        print("init")
        if t1 == None and t2 == None:
            return True

        # Cases where there is a mismatch between final tree nodes
        elif t1 == None or t2 == None:
            return False
        elif t1.val != t2.val:
            return False        

        # Recurse both left and right
        return self.recurseFind(t1.left, t2.left) and self.recurseFind(t1.right, t2.right)

z = Solution()
a = TreeNode(3)
b1 = TreeNode(4)
b2 = TreeNode(5)
c1 = TreeNode(1)
c2 = TreeNode(2)
d1 = TreeNode(0)

bfake1 = TreeNode(4)
bfake2 = TreeNode(5)
cfake1 = TreeNode(1)
cfake2 = TreeNode(2)
dfake1 = TreeNode(2)

bfake1.left = cfake1
bfake1.right = cfake2
cfake2.left = dfake1

a.left = b1
a.right = b2
b1.left = c1
b1.right = c2

print(z.isSubtree(a, b1))






