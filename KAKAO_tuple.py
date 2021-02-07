def solution(s):
    answer = []
    s= s[1:len(s)-1]
    l = []
    temp = []
    start = 0
    
    for idx, x in enumerate(s):
        if x == '{':
            start = idx + 1
            continue
        elif x == '}':
            l.append(s[start: idx])    
    l.sort(key=lambda x: len(x))
   
    l  = list(map(lambda x : x.split(','),l))
    while l:
        a = l.pop(0)[0]
        answer.append(int(a))
        for x in range(len(l)):
            l[x].remove(a)
        
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))