class Solution:
    def add_depths(self, depth):
        max = 0
        for i in depth:
            max+=i
        return max
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        arr = input.splitlines()
        depth = [0]
        max = 0
        depth_index = 0
        for i in arr:
            # print("i", i)
            depth_index = 0
            while i[0] == "\t":
                depth_index+=1
                i = i[1:]
                # print("\\t detected", i, depth_index)
            # print("depth index", depth_index, depth)
            if depth_index>=len(depth):
                # print("appended")
                depth.append(len(i)+1)
            else:
                depth[depth_index] = len(i)+1
            # print("depth", depth)
            if self.add_depths(depth[0:depth_index+1]) > max and '.' in i:
                max = self.add_depths(depth[0:depth_index+1])
                # print("max set", i)
        return max -1 if max > 0 else 0

a = Solution()
print(a.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
