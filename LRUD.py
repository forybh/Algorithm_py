def solution(N, d):
    start = [1, 1]
    for x in d:
        if x == 'R' and start[1] != N:
            start[1] += 1
            continue
        if x == 'L' and start[1] != 1:
            start[1] -= 1
            continue
        if x == 'U' and start[0] != 1:
            start[0] -= 1
            continue
        if x == 'D' and start[0] != N:
            start[0] += 1
            
    return start

print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))