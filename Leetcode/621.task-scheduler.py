import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Mathy solution
        # Generate busy and idle times using (n+1) * (most_frequent-1) items
        # If there are more tasks than spaces, they are guaranteed to fit into the generated
        # slots (think of ABC_AB__A...)
        # If there are less tasks than spaces, the number of elements with the same
        # max frequency gets added the the spaces count
        # Otherwise a solution would be to go through all frequencies and manually
        # decrement idle time
        freqs = collections.Counter(tasks)
        sorted_freqs = freqs.most_common()
        
        most_common = sorted_freqs[0][1]
        most_common_count = list(freqs.values()).count(most_common)

        print(n, most_common, most_common_count)
        return max(len(tasks), (n+1) * (most_common-1) + most_common_count)