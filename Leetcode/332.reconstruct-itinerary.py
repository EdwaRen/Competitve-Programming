import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
        graph = collections.defaultdict(list)

        for ticket in sorted(tickets)[::-1]:
            graph[ticket[0]].append(ticket[1])

        stack = ['JFK']
        route = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
        
z = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(z.findItinerary(tickets))

