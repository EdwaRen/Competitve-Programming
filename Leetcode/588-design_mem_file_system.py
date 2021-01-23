import collections

class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.content = ""


class FileSystem(object):

    def __init__(self):
        self.root = Node()


    def traverse(self, path):
        # Basic algorithm to traverse down to a designated path
        dirs = path.split('/')
        cur_storage = self.root
        for dir_name in dirs:
            if dir_name != '': 
                cur_storage = cur_storage.child[dir_name]
        return cur_storage


    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """

        # Get node at the end of the path
        dirs = path.split('/')
        cur_storage = self.traverse(path)

        # Return sorted results
        if cur_storage.content == '':
            return sorted([key for key in cur_storage.child.keys()])
        return [(dirs[-1])]
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """

        # Get node at the end of the path
        dirs = path.split('/')
        cur_storage = self.traverse(path)
                    

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """

        # Get node at the end of the path
        dirs = filePath.split('/')
        cur_storage = self.traverse(filePath)

        # Update file either with appended string or a new string
        if dirs[-1] in cur_storage.child:
            if isinstance(cur_storage.child[dirs[-1]], dict):
                cur_storage.child[dirs[-1]].content = [content]
            cur_storage.child[dirs[-1]].content.append(content)
        else:
            cur_storage.child[dirs[-1]].content = [content]
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """

        # Get node at the end of the path
        dirs = filePath.split('/')
        cur_storage = self.traverse(filePath)
        
        # Return file contents
        if dirs[-1] not in cur_storage.child: return null
        return "".join(cur_storage.child[dirs[-1]].content)


#Your FileSystem object will be instantiated and called as such:
path = '/'
dirPath = "/a/b/c"
filePath = "/a/b/c/d"
fileContent = "hello"

obj = FileSystem()
param_1 = obj.ls(path)
print(param_1)
obj.mkdir(dirPath)
obj.addContentToFile(filePath,fileContent)
print(obj.ls(path))
print(obj.readContentFromFile(filePath))

# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile","addContentToFile","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello world"],["/"],["/a/b/c/d"],["/a/b/c/d"," hello hello world"],["/a/b/c/d"]]

# z = FileSystem()
# print(z.ls('/'))
# z.mkdir("/a/b/c")
# z.addContentToFile("/a/b/c/d","hello world")
# print(z.ls("/"))
# print(z.readContentFromFile("/a/b/c/d"))
# z.addContentToFile("/a/b/c/d"," hello hello world")
# z.addContentToFile("/a/b/c/e"," 2hello hello world")
# z.addContentToFile("/dy","emer")

# print(z.readContentFromFile("/a/b/c/d"))
# print(z.ls("/a/b/c"))
# print(z.ls("/dy"))

# ["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","ls","ls","ls"]
# [[],["/goowmfn"],["/goowmfn"],["/"],["/z"],["/"],["/"],["/goowmfn/c","shetopcy"],["/z"],["/goowmfn/c"],["/goowmfn"]]


# ["FileSystem","mkdir","ls","mkdir","ls","ls","ls","addContentToFile","ls","ls","ls"]
# [[],["/m"],["/m"],["/w"],["/"],["/w"],["/"],["/dycete","emer"],["/w"],["/"],["/dycete"]]

# z = FileSystem()
# z.mkdir('/m')
# print(z.ls('/m'))
# z.mkdir("/w")
# print(z.ls('/'))
# print(z.ls('/w'))
# print(z.ls('/'))
# z.addContentToFile("/dycete","emer")
# print(z.ls('/w'))
# print(z.ls('/'))
# print(z.ls('/dycete'))
