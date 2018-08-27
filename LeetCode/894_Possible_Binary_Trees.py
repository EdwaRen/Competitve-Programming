# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        trees = [[]]
        trees.append([TreeNode(0)])
        for i in range(2, N+1):
            trees.append([])
            if i % 2 == 0:
                continue
            for j in trees[i-2]:
                t = TreeNode(0)
                t.left = j
                t.right = TreeNode(0)
                trees[i].append(t)
                t2 = TreeNode(0)
                t2.right = j
                t2.left = TreeNode(0)
                trees[i].append(t2)
        return trees[N]
a = Solution()
b = 3
res = a.allPossibleFBT(b)
for i in res:
    print("end print", i.val, i.left, i.right)
