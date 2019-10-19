import math
import heapq 

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """


        """
        Partition algorithm to find Kth largest element and sorts elements before and after relative to K
        """
        def partition(points, l, r):

            # Find euclid distance
            def euclid_dist(point):
                return point[0]**2 + point[1]**2

            # Initialize pivot_index to always be right-most point
            x = euclid_dist(points[r])
            i = l 

            # partitioning, swap when element smaller than pivot_index is found
            # x is still untouched
            for j in range(l, r):
                if euclid_dist(points[j]) <= x:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            # swap x back in place
            points[i], points[r] = points[r], points[i]
            return i

        """
        Finds Kth largest element by index, array is sorted by before/after K.
        Since elements before K are not sorted, this is still O(n)
        """
        def select(points, l, r, k):
            # Handle some edge cases
            if k >= len(points):
                return k

            # Get initial partition
            index = partition(points, l, r)

            # Refine partition each time
            if index == k:
                return index
            elif k < index:
                return select(points, l, index - 1, k)
            else:
                return select(points, index+1, r, k )

        # split_point is the Kth largest point to the origin
        # Everything before K is guaranteed to be closer to the origin than K
        split_point = select(points, 0, len(points)-1, K)
        return points[0:split_point]


z = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(z.kClosest(points, k))

        
