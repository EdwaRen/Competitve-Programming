from operator import itemgetter

class Solution(object):
    def reconstructQueue(self, people):
        arr = [None]*len(people)
        p_sorted = sorted(people, key=itemgetter(1), reverse=True)
        p_sorted = sorted(p_sorted, key=itemgetter(0), reverse=False)
        mem_empty = [i for i in range(len(p_sorted))]
        print("meme empty", mem_empty)
        for i in p_sorted:
            arr[mem_empty[i[1]]] = i
            mem_empty.pop(i[1])
        return arr
