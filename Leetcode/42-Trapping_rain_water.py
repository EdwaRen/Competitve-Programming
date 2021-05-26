class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        Two pointers, traveling both sides and recording max height of water
        """
        if len(height) < 1: return 0
        
        max_left, max_right = 0, 0
        left, right = 0, len(height)-1
        water_filled = 0
        
        while left <= right:
            if max_left <= max_right:
                max_left = max(max_left, height[left])
                water_filled += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                water_filled += max_right - height[right]
                right -= 1
                
        return water_filled
