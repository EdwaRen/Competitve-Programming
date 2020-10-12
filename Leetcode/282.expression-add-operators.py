class Solution(object):
    def addOperators(self, num, target):

        self.res = []

        def recurse(cur_sum, prev, str_val, index, num, target):

            # Base case
            if cur_sum == target and index == len(num):
                self.res.append(str_val[1:])

            cur_val = 0
            for sub in range(index, len(num)):
                cur_val = cur_val*10 + int(num[sub])
                
                # Always recurse for addition
                recurse(cur_sum+cur_val, cur_val, str_val + "+" + str(cur_val),  sub+1, num, target)
                
                # Only recurse for sub/multi if not the first number
                if index > 0:
                    recurse(cur_sum-cur_val, -cur_val, str_val + "-" + str(cur_val), sub+1, num, target)
                    recurse(cur_sum-prev + (prev*cur_val), prev*cur_val, str_val + "*" + str(cur_val), sub+1, num, target)
                
                # Handle edge case, multi digit number cannot start with zero
                if index == sub and num[index] == '0':
                    break 

        recurse(0, 0, '', 0, num, target)

        return self.res 

def addOperators(num, target):
    z = Solution()
    return(z.addOperators(num, target))

# num = "105"
num = "3456237490"
target = 9191
print(addOperators(num, target))

