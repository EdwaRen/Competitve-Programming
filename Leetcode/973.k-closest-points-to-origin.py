class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Find euclidean distances
        distance_points = [(self.find_euclidean(point, [0, 0]), point[0], point[1]) for point in points]
        
        # Quickselect to sort the distance points
        self.quickselect(distance_points, 0, len(distance_points)-1, k)
        return [[i[1], i[2]] for i in distance_points[:k]]
            
        
    def find_euclidean(self, x, y):
        return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5   
        
    def quickselect(self, distances, lo, hi, k):
        
        if k >= len(distances): return
        
        # Partition based on the last index, return index of where the last item fits
        index = self.partition(distances, lo, hi, k)
        
        # Quickselect with global index values
        if index == k:
            return
        elif index < k:
            self.quickselect(distances, index+1, hi, k)
        elif index > k:
            self.quickselect(distances, lo, index-1, k)
            
    def partition(self, distances, lo, hi, k):
        
        pivot = hi
        left = lo
        
        # Quickselect from lo to hi, move elements only if they are less than pivot
        for cur in range(lo, hi):
            if distances[cur][0] <= distances[pivot][0]:
                distances[left], distances[cur] = distances[cur], distances[left]
                left+=1

        # Put the pivot in its place
        distances[left], distances[pivot] = distances[pivot], distances[left]
                
        return left

                
        