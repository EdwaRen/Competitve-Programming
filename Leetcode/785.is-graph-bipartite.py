class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # DFS to determine bipartition
        # Sides is a dictionary that tracks the side a node is on (modeled as T/F)
        def dfs(node, graph, sides):
            sanitized = True
            if node not in sides:
                sides[node] = False

            for i in graph[node]:
                if i not in sides:
                    # Add side of children to be opposite of current side, then dfs
                    sides[i] = not sides[node]
                    sanitized = dfs(i, graph, sides) and sanitized

                elif sides[i] == sides[node]:
                    # conflict found
                    return False

            return sanitized 

        sides = {}
        # While we do iterate n times, everytime we visit an element we mark it and do not visit again.
        for i in range(len(graph)):
            if not dfs(i, graph, sides):
                return False
        return True

z = Solution()
graph = [[1, 3], [0,2], [1,3], [0,2]]
res = z.isBipartite(graph)
print(res)


        
