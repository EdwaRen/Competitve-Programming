"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # Dict mapping new -> old
        self.dp = {}

        stack = [node]

        def recurse(orig_node):
            if orig_node in self.dp:
                return self.dp[orig_node]
            else:
                created_node = Node(orig_node.val, [])
                self.dp[orig_node] = created_node

                for n in orig_node.neighbors:
                    created_node.neighbors.append(recurse(n))

                return created_node

        recurse(node)
        return self.dp[node]

z = Solution()
a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])

a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

res = z.cloneGraph(a)
seen = []
boomer_nodes = [a, b, c, d]

stack = [res]
while stack:
    cur_node = stack.pop()
    print(cur_node.val, cur_node in boomer_nodes, end='')
    for i in cur_node.neighbors:
        print(i.val, end = '')
        if i not in seen:
            stack.append(i)
            seen.append(i)
    print()

# print(res.val, res.neighbors)
# print(res == a)
                


            

        
