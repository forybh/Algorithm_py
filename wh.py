from math import floor

def solution(w,h):
    answer = 0
    
    for x in range(w-1, 0, -1):
        answer += floor(x * (h/w))
        if x * (h/w) < 1:
            break
    answer *= 2
    
    return answer

print(solution(5,3))