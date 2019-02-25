class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

def countSubstrings(S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        print('#'.join(S))
        Z = [0] * len(A)
        center = right = 0
        print("entering loop")
        for i in range(1, len(A) - 1):
            print("iter ", i, Z, right, center)
            if i < right:
                print("right activated")
                Z[i] = min(right - i, Z[2 * center - i])
            print(Z[i], A)
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            print(Z[i], A[i])
            if i + Z[i] > right:
                print("i + z[i] activated")
                center, right = i, i + Z[i]
            print(Z[i])
        return Z
    res = manachers(S)
    print(res)
    return sum((v+1)/2 for v in res)

arr = "abcaaaaac"
countSubstrings(arr)
