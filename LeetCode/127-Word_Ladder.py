import queue


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        def valid_change(a, b):
            arr = [0]*26
            woops = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    woops+=1
            return woops == 1 and len(a) == len(b)

        wordstack = {i: i for i in wordList}
        q = queue.Queue()
        q.put(beginWord)
        dist = 1
        #print("valid mist", valid_change("miss", "mist"))
        while q.empty() == False:
            size = q.qsize()
            for i in range(size):
                temp = q.get()
                #print(temp, wordstack)
                wordstacktemp = dict(wordstack)
                for i in wordstacktemp:
                    #if i == "miss":
                        #print("miss in stack", i, temp, wordstack)
                        #print("miss in stack", i in wordstack, valid_change(i, temp))

                    if i in wordstack and valid_change(i, temp):
                        #print("put in stack", i)
                        q.put(i)
                        if i == endWord:
                            return dist+1
                        del wordstack[i]
            dist+=1
        return 0

a = Solution()

b = "lost"
c = "miss"
w = ["most","mist","miss","lost","fist","fish"]
b = 'hit'
c = 'cog'
w = ["hot","dot","cot","lot","log"]
print(a.ladderLength(b, c, w))
