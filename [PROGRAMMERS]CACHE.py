

def solution(cacheSize, cities):
    answer = 0
    q = []
    if cacheSize == 0:
        return 5 * len(cities)
    for i in range(len(cities)):
        tmp = ''
        for c in cities[i]: #소문자로 변환
            if ord(c) < 97:
                tmp += chr(ord(c)+32)
            else:
                tmp += c
                
        cities[i] = tmp       
        if len(q) < cacheSize: #캐시에 빈자리가 있을 때
            if cities[i] not in q: #miss
                answer += 5
                q.append(cities[i])
            else: # hit
                answer += 1
                tmp = q.pop(q.index(cities[i]))
                q.append(tmp)
        else:
            if cities[i] in q: #hit
                answer += 1
                tmp = q.pop(q.index(cities[i]))
                q.append(tmp)
            else: 
                answer += 5
                q.pop(0)
                q.append(cities[i])
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))