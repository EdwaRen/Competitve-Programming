import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisite):
        course_map = collections.defaultdict(list)
        for i in range(len(prerequisite)):
            course_map[prerequisite[i][0]].append(prerequisite[i][1])
        # print(course_map)
        courses = set([key for key in course_map])
        # print(courses)
        for item in courses:
            # print("high level iter", key)
            if not self.dfs(prerequisite, item, {}, course_map):
                return False
            # print("course map high", course_map)
        return True

    def dfs(self, graph, index, seen, course_map):
        if index in seen and seen[index] == True:
            # print("seen false", index, seen)
            return False

        if index not in (course_map):
            return True
        seen[index] = True
        for pointer in course_map[index]:
            # print("pointer", index, pointer, course_map)
            if not self.dfs(graph, pointer, seen, course_map):
                # print("dfs false", pointer, seen, index)

                return False
        seen[index] = False
        return True


a = Solution()
size = 8
arr = [[1,0],[2,6],[1,7],[6,4],[0,1],[0,5]]

print(a.canFinish(size, arr))
