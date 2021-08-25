# 1. 최대로 많이 겹치는 부분
# 2. 단속 된 것 표현하기

def solution(routes):
    answer = 1
    cracked = [0 for x in range(len(routes))]
    cracked[0] = 1
    routes.sort(key = lambda x : x[0])
    start = routes[0][0]
    end = routes[0][1]
    for i, route in enumerate(routes):
        if cracked[i] == 0 and route[0] >= start and route[0] <= end:
            start = route[0]
            end = min(end, route[1])
            cracked[i] = 1
        elif cracked[i] == 1:
            continue
        else:
            answer += 1
            start = route[0]
            end = route[1]
            cracked[i] = 1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))