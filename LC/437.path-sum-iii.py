# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        Basically keeps a dictionary that stores the frequency of occurances of
        previous sums. Dictionary allows O(1) lookup times vs array of O(n).
        Match is found by using current_branch_sum - target_sum and seeing if
        that result is in the dictionary
        """
        # Hash is init to 0:1 to handle the root node being a match
        hash = {0:1}
        self.res = 0
        self.sum = sum

        # Recurse
        self.recurse(root, hash, 0)

        return self.res

    def recurse(self, root, hash, current_sum):
        # Handle base case
        if not root:
            return

        # Update current sum
        current_sum += root.val

        # Lookup the difference in the hash table
        self.res += hash.get(current_sum - self.sum, 0)
        hash[current_sum] = hash.get(current_sum, 0) +1

        # Recurse
        self.recurse(root.left, hash, current_sum)
        self.recurse(root.right, hash, current_sum)

        # New branch, cache is updated
        # current_sum is not updated since it is passed by_val while hash is passed by_ref
        hash[current_sum] -=1

z = Solution()
a = TreeNode(10)
b1 = TreeNode(5)
b2 = TreeNode(-3)
c1 = TreeNode(3)
c2 = TreeNode(2)
c3 = TreeNode(11)
d1 = TreeNode(3)
d2 = TreeNode(-2)
d3 = TreeNode(1)
a.left = b1
a.right = b2
b1.left = c1
b1.right = c2
b2.right = c3
c1.left = d1
c1.right = d2
c2.right = d3

print(z.pathSum(a, 10))
