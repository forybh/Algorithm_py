def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for n in new_id:
        
        if (ord(n) >= 97 and ord(n) <= 122) or (ord(n) >= 48 and ord(n) <= 57) or n == '-' or n == '_' or n == '.':
            answer += n

    while '..' in answer:
        index = answer.find('..')
        if index != -1:
            answer = answer[:index] + answer[index+1:]
    if answer[0] == '.' :
        answer = answer[1:]
    if len(answer) == 0 :
        answer = 'a'
    if answer[-1] == '.' :
        answer = answer[:-1]
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.' :
        answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
        
        
    return answer

print(solution("=.="))