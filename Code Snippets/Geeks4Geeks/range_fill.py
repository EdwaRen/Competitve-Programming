from collections import deque

def range_fill_percent(n, prefixes):
    total_time = 0
    prev = 0
    for i in range(len(prefixes)):
        total_time += prefixes[i][1] - max(prefixes[i][0], prev) + 1
        prev = prefixes[i][1] + 1

    return total_time * 100 / n 

def range_fill_overflows(n, prefixes):
    total_time = 0
    prev = 0
    overflows = []
    for i in range(len(prefixes)):
        total_time += prefixes[i][1] - max(prefixes[i][0], prev) + 1
        if prev - prefixes[i][0] > 0:
            overflows.append([ prefixes[i][0], prev-1])
        prev = prefixes[i][1] + 1

    return (total_time * 100 / n, overflows)

def dfs(n, valid_prefixes, candidate_prefixes):
    if range_fill_percent(candidate_prefixes):
        return True
    for prefix in valid_prefixes:
        if range_fill_percent(valid_prefixes.pop()):
            pass
    return False


def range_sum(n, prefixes, doubleup):
    prefixes.sort(key=lambda x: (x[1], x[0]))
    print(prefixes)
    if not doubleup:
        percent_time = range_fill_percent(n, prefixes)
        return percent_time
    else:
        percent_time, overflows = range_fill_overflows(n, prefixes)
        print(overflows)
        if percent_time >= 100.0 and range_fill_percent(n, overflows) == 100.0:
            return 100.0
        return 0.0
        
    

# n = 5
# prefixes = [[3, 4]]
# print(n, prefixes, range_sum(n, prefixes, False))

# n = 5
# prefixes = [[3, 4], [2, 4]]
# print(n, prefixes, range_sum(n, prefixes, False))

# n = 5
# prefixes = [[3, 4], [0, 4]]
# print(n, prefixes, range_sum(n, prefixes, False))
    
# n = 5
# prefixes = [[3, 4], [0, 4], [1, 2]]
# print(n, prefixes, range_sum(n, prefixes, True))
    
n = 5
prefixes = [[3, 4], [0, 4], [0, 1]]
print(n, prefixes, range_sum(n, prefixes, True))
    