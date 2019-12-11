#
# Complete the 'palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindrome(s):
    #O(n^2) solution
    # res = 0 # default response
    # for middle in range(len(s)*2-1):
    #     l = middle/2
    #     r = l + middle

    # Manacher's algorithm can be used instead


    # Breaking chars used to match both sides from the center
    middle = 0
    right = 0
    bounds = '@#' + '#'.join(s) + '#$'
    b = bounds
    res_arr = [0] * len(bounds)
    r = res_arr
    print(res_arr[0])
    print(bounds[0])

    for m in range(1, len(res_arr) -1):
        if m < right:
            res_arr[m] = min(right - m, res_arr[middle*2 - m])
        while bounds[m + res_arr[m] + 1] ==bounds[m - res_arr[m]-1] :
            res_arr[m] +=1
        if right < res_arr[m] + m:
            right = m + res_arr[m]
            middle = m


    return sum((m+1)/2 for m in (res_arr))


print(palindrome("aabaa"))
