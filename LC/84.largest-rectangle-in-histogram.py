class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                a = stack.pop()
                max_area = max(max_area, heights[a] * (i - stack[-1] -1 ))
            stack.append(i)
        return max_area

z = Solution()
arr = [2,1,5,6,2,3]
print(z.largestRectangleArea(arr))
