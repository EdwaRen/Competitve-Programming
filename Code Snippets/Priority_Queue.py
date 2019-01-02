import Queue as Q
q = Q.PriorityQueue()

q.push((3, 5))
print(q.get()) # there is not q.peak with this implementation
print(q.empty())
