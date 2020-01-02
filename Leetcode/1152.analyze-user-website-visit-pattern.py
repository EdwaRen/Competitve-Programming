import collections
import itertools 

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]

        Very smart solution ripped off of LC discussion forums
        We use min (-count[k], k) at the end to get the highest lexicographic count
          since items with the same count get sorted on k
        Would be good to see refresh zip() and itertools.combinations work in Code Snippets/
        """
        
        # Get a sorted mapping user => website 
        history = collections.defaultdict(list)
        for time, user, web in sorted(zip(timestamp, username, website)):
            history[user].append(web)
        
        # Count all possible subsequences
        count = collections.Counter()
        for key, value in history.items():
            # We have to use set() because non-distinct values can lead to repeated combinations
            count += collections.Counter(set(itertools.combinations(value, 3)))

        # Make sure we get the lexicographically smallest
        return min(count, key=lambda k: (-count[k], k))





z = Solution()
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["cart","maps","home","home","cart","maps","home","home","about","career"]

# username = ["u1","u1","u1","u2","u2","u2"]
# timestamp = [1,2,3,4,5,6]
# website = ["a","b","a","a","b","c"]

# username = ["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
# timestamp = [436363475,710406388,386655081,797150921]
# website = ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]

print(z.mostVisitedPattern(username, timestamp, website))
        
        
