class Solution(object):
    def generate(self, numRows):
        res = [  ] 

        # Iterate through all rows
        for i in range(numRows):

            # Handle special 0 case
            if i == 0:
                res.append([1])
            
            # Create new list on last-most list, append to res
            else:
                new = [1]
                for j in range(1, len(res[i-1])):
                    new.append( (res[i-1][j-1] + res[i-1][j]) )

                new.append(1)
                res.append(new)

        return res

z = Solution()
n = 6
print(z.generate(n))



 
