
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

print("Heapq implementation")
import heapq
nums = [4, 5, 1, 2, 7, 8, 3]
heapq.heapify(nums)
heapq.heappush(nums, 9)
print("return smallest:", 0)
print(heapq.heappushpop(nums, 0))
print("return 2nd smallest:", 1)
print(heapq.heappushpop(nums, 9))


