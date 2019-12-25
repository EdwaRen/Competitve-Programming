import collections

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        cum_freq = [0 for i in range(121)]
        num_freq = [0 for i in range(121)]
        for i in ages:
            num_freq[i]+=1

        for i in range(1, len(num_freq)):
            cum_freq[i] = cum_freq[i-1] + num_freq[i]

        friends = 0
        for i in ages:
            friends += max(cum_freq[i] - cum_freq[int(0.5*i)+7] -1, 0)        

        return friends 

z = Solution() 
ages = [20,30,100,110,120]
# ages = [16, 17, 18]
# ages = [101,56,69,48,30]
# ages = [8,85,24,85,69]
res = z.numFriendRequests(ages)
print(res)
            

        
