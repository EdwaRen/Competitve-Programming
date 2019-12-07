class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        # Find closed Intersection between two points
        def get_intersect(range1, range2):
            start = max(range1[0], range2[0])
            end = min(range1[1], range2[1])
            return [start, end]
        

        # Use two pointers for both lists
        res = []
        line_a = 0
        line_b = 0

        while line_a < len(A) and line_b < len(B):

            # Find intersection, only add if it is valid
            intersection = get_intersect(A[line_a], B[line_b])
            if intersection[0] <= intersection[1]:
                res.append(intersection)

            # Increase a pointer based on which ends sooner since the list is sorted
            if A[line_a][1] < B[line_b][1]:
                line_a+=1
            else:
                line_b+=1

        return res
            
z = Solution()
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(z.intervalIntersection(A, B))
        
