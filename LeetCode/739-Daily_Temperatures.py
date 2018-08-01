class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(T)
        for i in xrange(len(T)-1, -1, -1):
            print("iterate", i, T[i], stack)
            while len(stack) > 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = (stack[-1] - i)
            stack.append(i)
        # print("res", res[::-1])
        # print("stack", stack)
        return res

a = Solution()
b = [73, 74, 75, 71, 69, 72, 76, 73]
# b = [89,62,70,58,47,47,46,76,100,70]
print(a.dailyTemperatures(b))
