class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height)-1
        right_max = 0
        left_max = 0
        ans=0
        while left <= right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans+=left_max - height[left]
                left+=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans+= right_max-height[right]
                right-=1
        return ans

a = Solution()
print(a.trap([0, 1,0, 2, 1, 0,1, 3, 2, 1, 2, 1]))
