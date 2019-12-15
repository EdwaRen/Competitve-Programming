import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        # Init graph, pop_stack for topological sort.
        # frequencies is used to calculate pop_stack
        graph = collections.defaultdict(set)
        frequencies = collections.defaultdict(int)
        pop_stack = set()

        # Create 2D graph for topological sort
        # Uses a set to avoid duplicates messing with things
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                a = words[i][j]
                b = words[i+1][j]
                if a != b:
                    if b not in graph[a]:
                        frequencies[b]+=1
                    graph[a].add(b)
                    break 

        # Find base elements to pop in topological sort
        letters = set("".join(words))
        for letter in letters:
            if letter not in frequencies:
                pop_stack.add(letter)

        # Topological sort
        topo_sort = []
        while pop_stack:
            base = pop_stack.pop()
            topo_sort.append(base)
            for letter in graph[base]:
                frequencies[letter]-=1
                if frequencies[letter] == 0:
                    pop_stack.add(letter)

        if len(set(topo_sort)) != len(letters):
            return ""
        return "".join(topo_sort)
        
        
z = Solution()
words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
words = ['z', 'x']
words = ['z', 'x', 'z']
words = ["za","zb","ca","cb"]
# words = ["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
print(z.alienOrder(words))