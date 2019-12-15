class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []

        def recurse(cur_sum, prev, current, index, op_string, target, num):
            if index >= len(num):
                if cur_sum  == target:
                    self.res.append(op_string)
            else:
                current = 0

                # Go through every possible multi digit operand
                for subindex in range(index, len(num)):

                    # current value
                    current = current*10 + int(num[subindex])

                    # Handle first case
                    if index == 0:
                        recurse(current, current, 0, subindex+1, str(current), target, num)
                    else:

                        # Addition + subtraction
                        recurse(cur_sum + current, current, 0, subindex+1, op_string + '+' + str(current), target, num)
                        recurse(cur_sum - current, -current, 0, subindex+1, op_string + '-' + str(current), target, num)

                        # Mult 
                        recurse(cur_sum - prev + (prev * current), prev * current, 0, subindex+1, op_string + '*' + str(current), target, num)

                    # Handle case of 00+2 or 01+5
                    if current == 0:
                        break

        recurse(0, 0, 0, 0, '', target, num)
        return self.res 
        
z = Solution()
num = '232'
target = 8


# num = "3456237490"
# target = 9191

# num = '105'
# target = 5

num = '000'
target = 0

print(z.addOperators(num, target))
        
