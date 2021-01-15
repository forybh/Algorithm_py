def solution(x):
    s = sum(map(int, str(x)))
        
    return x % s == 0

print(solution(11))