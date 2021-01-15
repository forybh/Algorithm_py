def solution(N):
    answer = 0
    for i in range(N+1):
        if i != 3 and i != 13 and i != 23:
            answer += 15 * 45 + 15 * 45 + 15 * 15
        else: 
            answer += 60 * 60
    return answer
        

print(solution(5))