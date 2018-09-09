class Solution(object):
    def findLadders(self, source, end, wordList):

        def bfs(start, end, forward, tree, wordList):
            if not start:
                return False

        paths = collections.defaultdict(list)
        path = []
        tree = [source]
        found = self.bfs(set([source]), set([end]), True, tree, wordList)

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
