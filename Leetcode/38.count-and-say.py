class Solution(object):
    def countAndSay(self, n):
        # res is the code after every iteration from 1 - n
        res = '1'

        # Generate the code n times
        for j in range(n-1):
            
            # Keep track of new code
            cur = '' 
            count = 1
       
            # Generate the code for the current number
            for i in range(len(res)):
                
                # res[i] and res[i+1] checks for consecutive equal numbers
                if i+1 < len(res) and res[i] == res[i+1]:
                    count+=1

                # non-consecutively equal numbers, new data appended to cur
                else:
                    cur+= str(count) + res[i]
                    count = 1

            # Update res variable
            res = cur

        return res

# z = Solution()
# n = 5
# print(z.countAndSay(n))


