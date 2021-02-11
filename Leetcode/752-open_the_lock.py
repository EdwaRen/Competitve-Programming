import collections

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        Use a BFS to find the minimum number of moves. This is a case where a BFS
        is preferable to a DFS because we can guaranteed the closest combo
        """

        if "0000" in deadends:
            return -1
        visited = set(deadends)

        queue = collections.deque([("0000")])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return depth
                for i in range(len(cur)):
                    left, right = cur[:i], cur[i+1:]
                    for j in [-1, 1]:
                        next_combo = left + str((int(cur[i]) + j) % 10) + right
                        if next_combo not in visited:
                            visited.add(next_combo)
                            queue.append(next_combo)

            depth += 1
        return -1


z = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

deadends = ["8888"]
target = "0009"
#
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
#
# deadends = ["0001", "0009"]
# target = "8888"

print(z.openLock(deadends, target))
