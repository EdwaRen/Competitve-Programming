class Solution:
    def leastInterval(self, tasks, n):
        most_common = 0
        letter_count = [0] * 26
        print(letter_count)
        for i in tasks:
            char_id = ord(i)-65
            print(char_id)
            letter_count[char_id]+=1
            if letter_count[char_id] > most_common:
                most_common = letter_count[char_id]

        open_spaces = (most_common-1)*n

        if len(tasks) > open_spaces + most_common:
            return len(tasks)
        else:
            res = open_spaces+most_common
            for i in range(0, 26):
                if letter_count[i] == most_common:
                    res+=1
            return res -1

a = Solution()
print(a.leastInterval(["A","A","A","B", "C", "D", "E", "F"], 2))
