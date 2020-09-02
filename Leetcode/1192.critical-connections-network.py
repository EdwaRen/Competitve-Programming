import collections 

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        G = collections.defaultdict(set)
        for i in connections:
            G[i[0]].add(i[1])
            G[i[1]].add(i[0])
           

        first_seen = [-2] * n
        connections = set([tuple(sorted([x[0], x[1]])) for x in connections])
        def dfs(current, n, first_seen, G, connections, depth):
            if first_seen[current] >= 0:
                return first_seen[current]
            
            first_seen[current] = depth
            min_child_depth = n

            for connect in G[current]:
                if first_seen[connect] == depth - 1:
                    continue

                child_depth = dfs(connect, n, first_seen, G, connections, depth+1)  
                if child_depth <= depth:
                    connections.remove(tuple(sorted([current, connect])))

                min_child_depth = min(min_child_depth, child_depth)
            first_seen[current] = n
            return min_child_depth

        dfs(0, n, first_seen, G, connections, 0)
        return list(connections)

connections = [[0,1],[1,2],[2,0],[1,3]]
z = Solution()
print(z.criticalConnections(len(connections), connections))