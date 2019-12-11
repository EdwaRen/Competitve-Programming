import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        
        # Create dictionary graph, edges represented by a list        
        course_map = collections.defaultdict(list)
        for i in prerequisites:
            course_map[i[0]].append(i[1])

        # Create global variables to use during recursion 
        self.temp = set()
        self.perm = set()
        self.sort_order = []
        self.valid = True

        # Recurse through each course
        # self.perm acts as DP to keep it O(n) and tracks already visited nodes
        # self.temp enables breakout from cyclical packages
        # self.valid records cyclical graphs
        # self.sort_order is what we return
        def visit(course, course_map):
            
            # Handle base cases
            if course in self.perm:
                return
            if course in self.temp:
                return -1
            
            # Set temp and recurse
            self.temp.add(course)
            for i in course_map[course]:
                
                # The entire thing with local_res is to detect cycles
                local_res = visit(i, course_map)
                if local_res == -1:
                    self.valid = False

            # Reset temp and add to perm
            self.temp.remove(course)
            self.perm.add(course)
            self.sort_order.append(course)

        # Iterate through all valid course requirements
        list_of_course_keys = list(course_map.keys())
        for i in list_of_course_keys:    
            visit(i, course_map)    
   
        # Handle no prereq courses 
        for i in range(numCourses):
            if i not in self.sort_order:
                self.sort_order.append(i)
        
        # Handle invalid case
        if not self.valid:
            return []
        return self.sort_order

z = Solution()
#m = [[1,0],[2,0],[3,1],[3,2]]
m = [[1, 0]]
n = 2
print(z.findOrder(n, m))


