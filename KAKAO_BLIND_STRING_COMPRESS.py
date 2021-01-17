def solution(s):
    answer = 0
    result = []
    if len(s) == 1:
        return 1
    for n in range(1, int(len(s)/2) + 1):
        temp = ''
        count = 1                                
        for i in range(0, len(s), n):
            if len(s[i:]) < n:
                temp += s[i:]
                break
            if s[i:i+n] == s[i+n:i+2*n]:
                count += 1
            else:
                if count != 1:
                    temp += str(count)
                temp += s[i:i+n]
                count = 1
        result.append(len(temp))

    answer = min(result)            
    return answer

print('anwer = ', solution("x"))