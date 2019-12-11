class Solution(object):
    def strStr(self, txt, pat):

        def search(pat, txt):
            N = len(pat)
            M = len(txt)
           
            if pat == "":
                return 0
 
            for i_idx, i_txt in enumerate(txt):
                if i_idx+N <= M and  txt[i_idx: i_idx+N] == pat:
                    return i_idx
    
            return -1




        def searchkmp(pat, txt):

            # Handle edge cases
            if pat == "":
                return 0
            if txt == "":
                return -1
                

            # Define lengths
            N = len(pat)
            M = len(txt)

            # Create lps array
            lps = [0] * len(pat)
            kmpCreateLps(pat, N, lps)

            # i iterates through the txt, j iterates through the pattern we are finding
            i = 0
            j = 0

            # Iterate through all of txt
            while i < M:
                # Match, increase both i and j
                if txt[i] == pat[j]:
                    i+=1
                    j+=1

                # The pattern completely matches, return 
                if j == N:
                    return i - N

                # Similar to LPS, but we have a case where we don't increemnt i or j
                if i < M and txt[i] != pat[j]:
                    # J is not set to 0 becasue the lps[j-1] characters already match
                    if j != 0:
                        j = lps[j-1]
                    else: 
                        i+=1


            return -1

        def kmpCreateLps(pat, N, lps):
            # len is the longest prefix that is matching
            len = 0
            
            # i is the end bounding character
            i = 1

            # Traverse the string to construct lps array
            while i < N:

                # Match. Increase len, i, and set lps to len
                # This is the only time lps will increase
                if pat[len] == pat[i]:
                    len += 1
                    lps[i] = len
                    i +=1
                else:
                    # No match, check if a smaller suffix will match
                    # Notice we don't increment i
                    # Decrease len and check again during next loop iteration
                    if len != 0:
                        len = lps[len-1]
                    # No match and no possible smaller suffixes. Set to 0
                    else:
                        lps[i] = 0
                        i+=1

        return search(pat, txt)

z = Solution()
pat = "ll"
txt = "hello"
print(z.strStr(txt, pat))


