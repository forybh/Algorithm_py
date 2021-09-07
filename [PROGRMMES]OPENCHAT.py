def solution(record):
    answer = []
    process = []
    d = {}
    
    for r in record:
        p = r.split()
        if p[0] == 'Enter': #입장
            d[p[1]] = p[2]
            process.append((p[0], p[1]))
            
        elif p[0] == 'Leave': #퇴장
            process.append((p[0], p[1]))
        else: #변경
            d[p[1]] = p[2]
            
    for pro in process:
        tmp = d[pro[1]] + "님이 "
        if pro[0] == 'Enter':
            tmp += "들어왔습니다."
        else:
            tmp += "나갔습니다."
        answer.append(tmp)
       
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))