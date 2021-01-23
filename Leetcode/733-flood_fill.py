class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        # Catch edge case
        if not image or len(image) == 0:
            return None

        # Cache commonly used expressions
        N = len(image)
        M = len(image[0])
        orig_color = image[sr][sc]
        seen = set()

        # BFS
        queue = [(sr, sc)]
        while queue:
            row, col = queue.pop(0)
            image[row][col] = newColor
            
            for dir in [[row+1, col], [row, col+1], [row-1, col], [row, col-1]]:
                if dir[0] >= N or dir[0] < 0 or dir[1] >= M or dir[1] < 0:
                    continue
                if image[dir[0]][dir[1]] == orig_color and str(dir[0]) + "," + str(dir[1]) not in seen:
                    seen.add(str(dir[0]) + "," + str(dir[1]))
                    queue.append((dir[0], dir[1]))
        return image

image = [
[1, 1, 1],
[1, 1, 0],
[1, 0, 1],
]

z = Solution()
res = z.floodFill(image, 1, 1, 1)
for i in res:
    print(i)

