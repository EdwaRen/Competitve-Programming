import collections

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        mapping = collections.defaultdict(list)

        # Parse input
        for directory in paths:
            paths = directory.split(" ")
            dir_path = paths[0]

            # Map contents to it's path
            for file_all in paths[1:]:
                file_path = file_all.split('(')[0]
                file_contents = file_all.split('(')[1][0:-1]
                mapping[file_contents] += [dir_path+'/'+file_path]
        
        res = []
        
        # Get all directories where more than content maps to more than 1 directory
        for key, val in mapping.items():
            if len(val) > 1:
                res.append(val)
        return res 

z = Solution()
files = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(z.findDuplicate(files))