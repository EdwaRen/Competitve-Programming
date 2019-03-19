# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
#def knows(a, b):
#    return True

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Candidate variable
        cand = 0

        # Find candidate, will stop once celebrity is hit since he/she doesn't know others
        for i in range(n):
            if knows(cand, i):
                cand = i
        
        # Check that the first 0-cand people aren't known by the celeb
        for i in range(0, cand):
            if knows(cand, i):
                return -1
    
        # Check remaining candidates to ensure they know celebrity, celeb is guaranteed to not know them from the first loop
        for i in range(cand, n):
            if not knows (i, cand):
                return -1
    
        return cand





 
