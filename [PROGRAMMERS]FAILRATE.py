def solution(N, stages):
    answer = []
    result = []
    arrive = [0] * (N+2)
    clear = [0] * (N+2)
    
    #arrive/clear가 실패율
    
    for stage in stages:
        for s in range(1, stage+1):
            clear[s] += 1
        arrive[stage] += 1
        
    for i in range(1,N+1):
        if arrive[i] + clear[i] == 0:
            answer.append((i,0))
        else:
            answer.append((i,arrive[i]/ clear[i]))
    answer.sort(key = lambda x: (-x[1], x[0]))      
    
    for ans in answer:
        result.append(ans[0])
      
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))