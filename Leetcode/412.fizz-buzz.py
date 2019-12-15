class Solution(object):
    def fizzBuzz(self, n):
        # Scaleable hash
        dict = {3:"Fizz", 5:"Buzz"}
        res = []

        # Iterate through 1-n+1
        for i in range(1, n+1):
            
            # app represents what to append of not the number
            app = "" 

            # iterate through any number of keys, instead of only 3, 5
            for j in [3, 5]:
                if not i % j:
                    app+=(dict[j])
            
            # Append to res array
            if app != "":
                res.append(app)
            else:
                res.append(str(i)) 
                   
        return res

z = Solution()
n = 15
print(z.fizzBuzz(n))
        











