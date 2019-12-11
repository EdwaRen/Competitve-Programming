class Solution(object):
    def uniquePaths(self, m, n):
        arr = [1] * (m)
        #arr[0] = 0
        #print(arr)
        for i in range(1, n):
            prev = 0
            for j in range(m):
                arr[j] = arr[j] + prev
                prev = arr[j]
            #print(arr)
        #print(arr)
        return arr[-1]

z = Solution()
m = 7
n = 3
print(z.uniquePaths(m, n))   






 
