import collections
from itertools import combinations
def solution(info, query):
    answer = []
    info = list(map(lambda x: x.split(), info))
    query = list(map(lambda x: x.split(), query)) #1 3 5sms and
    
    d = collections.defaultdict(list)
    
    for inf in info:
        key = inf[:-1]
        val = int(inf[-1])
        for i in range(5):
            for c in combinations(key,i):
                d["".join(c)].append(val)
    for k in d.keys():
        d[k].sort()
    
        
    for q in query:
        tmp = ''
        if q[0] != '-':
            tmp += q[0]
        if q[2] != '-':
            tmp += q[2]
        if q[4] != '-':
            tmp += q[4]
        if q[6] != '-':
            tmp += q[6]
        val = int(q[7])
        if len(d[tmp]) == 0 :
            answer.append(0)
            continue
        if len(d[tmp]) == 1 :
            if d[tmp][0] >= val:
                answer.append(1)
            else:
                answer.append(0)
            continue
        left = 0; right = len(d[tmp]);
        while left < right:
            mid = (left + right) // 2
            if d[tmp][mid] >= val:
                right = mid 
            else:
                left = mid + 1
        answer.append(len(d[tmp]) - left)
 
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))