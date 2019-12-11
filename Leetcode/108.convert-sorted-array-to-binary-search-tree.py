# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        # Handle base acse
        if len(nums) == 0:
            return None

        # Get mid of the array, split array in two halves
        mid = int(len(nums)/2)
        
        # Create new node
        cur_node = TreeNode(nums[mid])
        left, right = nums[:mid], nums[mid+1:]

        # Perform in order traversal
        cur_node.left = self.sortedArrayToBST(left)
        cur_node.right = self.sortedArrayToBST(right)
        return cur_node

    def print_bst(self, node, depth):
        if not node:
            return
        print(("  " * depth) + str(node.val))
        self.print_bst(node.left, depth + 1)
        self.print_bst(node.right, depth+1)

z = Solution()
nums = [-10, -3, 0, 5, 9]
res = z.sortedArrayToBST(nums)
print(z.print_bst(res, 1))

 
