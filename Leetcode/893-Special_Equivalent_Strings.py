class Solution(object):
    def numSpecialEquivGroups(self, A):
        #print("num special detected", A)
        def s_move(a, b):
            #print("s move", a, b)
            arr = [0]*26
            if len(a) != len(b):
                return False
            if (set(a) == set(b)):
                seg_a = a[0:][::2]
                seg_a2 = a[1:][::2]

                seg_b = b[0:][::2]
                seg_b2 = b[1:][::2]

                if (set(seg_a) == set(seg_b)) and (set(seg_a2) == set(seg_b2)):
                    return True
            return False
        groups = []
        for i in A:
            flag = False
            for j in groups:
                if s_move(i, j):
                    flag = True
                    break
            if flag == False:
                groups.append(i)
                #print("new group", groups)

        #print(groups)
        return len(groups)

a = Solution()
b = ["a","b","c","a","c","c"]
print(a.numSpecialEquivGroups(b))
