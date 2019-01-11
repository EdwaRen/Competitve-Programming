from collections import defaultdict
class Solution():
    def mostCommonWord(self, sentence, banned):
        exclude = set([a for a in "?!',;."])
        map = {}
        map = defaultdict(lambda:0, map)
        sentence = ''.join(ch for ch in sentence if ch not in exclude)
        for word in sentence.split():
            map[word.lower()]+=1
        for ban in banned:
            map[ban] = 0
        res = 0
        word = "i"
        for key, value in map.items():
            if value > res:
                res = value
                word = key
        return word

a = Solution()
b = "bob hit a ball, the hit BALL flew far after it was hit."
c = ["hit"]
print(a.mostCommonWord(b, c))
print("hello")
