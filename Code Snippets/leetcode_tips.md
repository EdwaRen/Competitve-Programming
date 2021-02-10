# Tips
- DFS is usually preferable to a BFS. However, if the number of moves has to be minimized
then a BFS is much more preferable. An example is 752 - Open the lock
- Both DFS and BFS can be implemented recursively, or with lists.
  - BFS should use a deque because in Python pop(0) is an O(n) operation
