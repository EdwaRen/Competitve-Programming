import string
import collections
class Solution(object):
    def findLadders(self, source, end, wordList):

        def dfs(source, end, tree):
            if source == end:
                return [[source]]
            return [[source] + path for each in tree[source] for path in dfs(each, end, tree)]

        def bfs(start, end, forward, tree, wordList):
            if not start:
                return False
            if len(start) < len(end):
                return bfs(end, start, not forward, tree, wordList)
            for i in set(list(start) + list(end)):
                wordList.discard(i)
            next = set()
            done = False
            while start:
                p = start.pop()
                for c in string.ascii_lowercase:
                    for i in range(len(p)):
                        new = p[:i] + c + p[i+1:]
                        if new in end:
                            done = True
                            if forward == True:
                                tree[p].append(new)
                            else:
                                tree[new].append(p)
                        if new in wordList and not done:
                            next.add(new)
                            if forward == True:
                                tree[p].append(new)
                            else:
                                tree[new].append(p)
            return done or bfs(next, end, forward, tree, wordList)

        tree = collections.defaultdict(list)
        if end not in wordList:
            return []
        found = bfs(set([source]), set([end]), True, tree, set(wordList))
        return dfs(source, end, tree)

s = Solution()
a = "hit"
b = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(s.findLadders(a, b, wordList))
print("end")
