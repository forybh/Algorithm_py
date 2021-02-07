def solution(p):
    answer = ''
    u = ''
    count = 0
    if len(p) < 2:
        return ''
    while True:
        if p[0] == '(':
            count += 1
            u += '('
            p = p.replace(p[0], '', 1)
        else:
            count -= 1
            u += ')'
            p = p.replace(p[0], '', 1)
        if count == 0:
            break
    if u[0] == '(' and u[-1] == ')':
        answer = u + solution(p)
    else:
        answer = '('
        answer += solution(p)
        answer += ')'
        u = u[1:len(u)-1]
        temp =''
        for x in u:
            if x == '(':
                temp += ')'
            else: temp += '('
        answer += temp
        
    return answer

print(solution(')()()()('))
