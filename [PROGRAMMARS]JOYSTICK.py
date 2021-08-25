def solution(name):
    answer = 0
    name = list(name)
    count = [0 for x in range(len(name))]
    for i, n in enumerate(name):
        if ord(n) < 78:
            answer += ord(n) - 65
        else:
            answer += 91 - ord(n) 
    current = 0
    target = ['A'] * len(name)
    name[0] = 'A'
    while name != target:
        print(name)
        go_current = current
        go = 0
        back_current = current
        while True:
            go += 1
            go_current = go_current + 1 if go_current + 1 < len(name) else 0
            back_current = back_current - 1 if back_current - 1 >= 0 else len(name) - 1
            if name[go_current] != 'A':
                answer += go
                current = go_current
                name[current] = "A"
                break
            if name[back_current] != 'A':
                answer += go
                current = back_current
                name[current] = "A"
                break
                            
    return answer

print(solution("JAN"))