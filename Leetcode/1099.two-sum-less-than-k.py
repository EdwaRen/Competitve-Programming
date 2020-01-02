class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        # Guard 
        if not A or not K or len(A) <= 1:
            return -1

        # Sort inputs
        inputs_sorted = sorted(A)

        # Two pointers through sorted input
        min_pointer = 0
        max_pointer = len(A)-1
        closest = -1

        # Keep updating pointers to keep getting as close to K as possible
        while min_pointer < max_pointer:
            cur_sum = inputs_sorted[min_pointer] + inputs_sorted[max_pointer]
            if cur_sum < K:
                closest = max(closest, cur_sum)
                min_pointer+=1
            elif cur_sum >= K:
                max_pointer-=1

        return closest

z = Solution()
A = [10,20,30]
K = 16
print(z.twoSumLessThanK(A, K))