
# THIS IS FOR PYTHON3

# Use this if python2
# import Queue as Q  # ver. < 3.0

import queue as Q
q = Q.PriorityQueue()

q.put((3, 5))
q.put((4, 2))

print("test")
print(q.get()) # there is not q.peak with this implementation
print(q.empty())
