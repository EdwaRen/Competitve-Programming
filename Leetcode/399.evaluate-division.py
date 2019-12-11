import collections

class Solution(object):
    def calcEquation(self, equations, values, queries):

        # Dictionary of dictionary that acts as a graph
        graph = collections.defaultdict(dict)       

        # Fill in the graph with the values we currently have
        for (num, den), val in zip(equations, values):
            graph[num][num] = 1
            graph[num][den] = val
            graph[den][num] = 1/val

        # Construct all possible paths from num to den
        def path_construct(num, den):

            # Deq is a deque the acts as an iterable BFS
            deq = [(num, 1)]
            seen = {}
            
            if num not in graph:
                return -1


            # Iterate through all possible permutations with the current numerator
            while deq:
                cur, prod = deq.pop(0)

                # Adds each popped character to seen to avoid looping back
                seen[cur] = 1

                # Base case, path found
                if cur == den:
                    return prod

                # Search through all possible connections to the current character from our graph's connections
                for key, val in graph[cur].items():
                    # Add if a valid node is found, add it to the stack and use it as the next numerator to search through
                    if key not in seen:
                        deq.append((key, prod*val))
    
            # Nothing found, return -1
            return -1

        return [ path_construct(i[0], i[1]) for i in queries ]

z = Solution()
eqns = [ ["a", "b"], ["b", "c"]]
vals = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(z.calcEquation(eqns, vals, queries))



