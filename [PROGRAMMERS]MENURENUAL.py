import collections
from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        d = collections.defaultdict(int)
        for order in orders:
            tmp = list(combinations(order, c))
            for t in tmp:
                t = list(t)
                t.sort()
                d["".join(t)] += 1
        if len(d) != 0:
            m = max(d.values())
        if m <= 1:
            continue
        for k in d.keys():
            if d[k] == m:
                answer.append(k)
    
    answer.sort()
            
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))