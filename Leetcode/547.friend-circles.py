class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(M, seen, person):
            for friend, friendship in enumerate(M[person]):
                if friendship == 1 and friend not in seen:
                    seen.add(friend)
                    dfs(M, seen, friend)

        groups = 0
        seen = set()
        N = len(M)
        for person in xrange(N):
            if person not in seen:
                seen.add(person)
                dfs(M, seen, person)
                groups+=1

        return groups

z = Solution()
M = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
 ]
print(z.findCircleNum(M))