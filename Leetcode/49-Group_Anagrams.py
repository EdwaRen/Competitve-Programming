class Solution:
    def groupAnagrams(self, strs):
        map = {}
        primes = []

        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)%26]+=1
            if str(arr) in map:
                map[str(arr)].append(i)
            else:
                map[str(arr)] = [i]
        return list(map.values())

a = Solution()
b = ["tin","ram","zip","cry","pus","jon","zip","pyx"]
b = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(a.groupAnagrams(b))
