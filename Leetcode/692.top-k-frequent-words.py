import collections
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        # Use counter to track frequency of words
        # Can reduce memory usage with a Trie where each node also stores frequency
        freq = collections.Counter(words)

        # Heapify in O(n)
        # Heapq comparator uses second tuple element if the first has an equal
        mapping = [(-freq[word], word) for word in freq]
        heapq.heapify(mapping)

        # Get k most frequenct using the heap O(N log k)
        return [heapq.heappop(mapping)[1] for _ in range(k)]

z = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(z.topKFrequent(words, k))



        
        
