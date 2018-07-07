class Solution(object):
    def anagramMappings(self, A, B):
        arr = {}
        for i in range(len(B)):
            arr[B[i]] = i
        return [arr[k] for k in A]

l1 = [12, 28, 46, 32, 50]
l2 = [50, 12, 32, 46, 28]
a = Solution()
print(a.anagramMappings(l1, l2))
