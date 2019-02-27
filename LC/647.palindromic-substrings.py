class Solution(object):

    def countSubstrings(self, S):
        res = 0

        # Account for centers in between characters
        for i in range((2*len(S))-1):
            left = int(i / 2)
            right = int((i+1)/2)

            # Perform expand and match at each center
            while left >= 0 and right < len(S):
                if S[left] == S[right]:
                    res +=1
                else:
                    left = -1
                left -=1
                right +=1

        return res

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

z = Solution()
arr = "fdsklf"
print(z.countSubstrings(arr))
