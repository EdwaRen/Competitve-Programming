
# THIS IS FOR PYTHON3

# Use this if python2
# import Queue as Q  # ver. < 3.0

import queue as Q
q = Q.PriorityQueue()

# Smaller keys get popped out first
q.put((3, 5))
q.put((4, 2))
q.put((1, 2))

print("test should return (1, 2)")
print(q.get()) # there is not q.peak with this implementation
print(q.empty())
