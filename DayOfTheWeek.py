def solution(a, b):
    answer = ''
    day = 0
    d1 = [1, 3, 5, 7, 8, 10, 12]
    d2 = [4, 6, 9, 11]
    
    for i in range(1, a+1):
        if i-1 in d1:
            day += 31
        elif i-1 in d2:
            day += 30
        elif i-1 == 2:
            day += 29
        else:
            continue
    
    day += b -1
    
    d = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    answer = d[day%7]
    return answer

print(solution(5,24))