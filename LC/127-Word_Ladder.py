import Queue as queue

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        alphabet = [str(unichr(i)) for i in range(97, 124)]
        wordstack = {i: i for i in wordList}
        if beginWord in wordstack:
            del wordstack[beginWord]
        q = queue.Queue()
        q.put(beginWord)
        dist = 1

        while q.empty() == False:
            size = q.qsize()
            for i in range(size):
                q_word = q.get()
                for index, letter in enumerate(q_word):
                    pre = q_word[:index]
                    suff = ""
                    if index < len(q_word):
                        suff = q_word[index+1:]
                    for j in alphabet:
                        new = pre + j + suff
                        if new in wordstack:
                            q.put(new)
                            if new == endWord:
                                return dist+1
                            del wordstack[new]
            dist+=1
        return 0

a = Solution()

b = "lost"
c = "miss"
w = ["most","mist","miss","lost","fist","fish"]
b = 'hit'
c = 'cog'
w = ["hot","dot","dog","lot","log", "cog", 'hog']
print(a.ladderLength(b, c, w))
