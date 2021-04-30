class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        Sort both lists and find the product
        """
        horizontals = sorted([0] + horizontalCuts + [h])
        verticals = sorted([0] + verticalCuts + [w])
        max_horizontal = 0
        max_vertical = 0
        for i in range(len(horizontals)-1):
            max_horizontal = max(max_horizontal, horizontals[i+1] - horizontals[i])

        for i in range(len(verticals)-1):
            max_vertical = max(max_vertical, verticals[i+1] - verticals[i])

        return (max_vertical * max_horizontal) % (10**9 + 7)

z = Solution()
h = 5
w = 4
hc = [3]
vc = [3]
print(z.maxArea(h, w, hc, vc))
