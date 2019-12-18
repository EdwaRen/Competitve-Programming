class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        stack = []
        overhead = [0]
        res = [0 for i in range(n)]

        for log_str in logs:
            log = log_str.split(':')
            if log[1] == 'start':
                overhead.append(0)
                stack.append(log)
            else:
                start_log = stack.pop()
                topped = overhead.pop()
                duration = int(log[2]) - int(start_log[2]) - topped + 1
                overhead[-1] += duration + topped
                res[int(log[0])] += duration
        return res 

z = Solution() 
n = 4
logs = ["0:start:0","1:start:2", "2:start:3", "2:end:4", "1:end:5","3:start:7", "3:end:9", "0:end:12"]

# n = 1
# logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]

# n = 1
# logs = ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
res = z.exclusiveTime(n, logs)
print(res)

        
