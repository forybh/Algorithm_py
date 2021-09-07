def solution(n, t, m, timetable):
    answer = ''
    time_list = []
    tmp_answer = 0
    for time in timetable: #시간 변환
        hour, minute = time.split(":")
        time_list.append(int(hour)*60 + int(minute))
    start = 540 # 9시 00분
    time_list.sort()
    onBus = [0] * n
    bus = 0
    i = 0
    
    while bus < n: #탈 수 있을 때
        if onBus[bus] < m and time_list[i] <= start:
            onBus[bus] += 1
        else: #못탈때 다음 버스로 바꾸기
            bus += 1
            start += t
            continue
        i += 1 
        if i >= len(time_list):
            break
    print(onBus)
    
    last = i - 1
    print(last)
    if onBus[-1] < m:
        tmp_answer = 540 + (t * (n-1))
    else:
        tmp_answer = time_list[last] - 1
        
    hour = tmp_answer // 60
    minute = tmp_answer % 60
    
    if(hour < 10):
        answer += '0' 
    answer += str(hour)
    answer += ':'
    if(minute < 10):
        answer += '0'
    answer += str(minute)
        
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))