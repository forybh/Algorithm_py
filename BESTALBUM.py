def solution(genres, plays):
    answer = []
    m = dict()
    m2 = dict()
            
    for i in range(len(plays)):
        if genres[i] not in m.keys():
            m[genres[i]] = [(plays[i],i)]
            m2[genres[i]] = plays[i]
        else :
            m[genres[i]].append((plays[i],i))
            m2[genres[i]] += plays[i]
    
    sort_m2 = sorted(m2.items(), key= lambda x: x[1])
    m3 = dict()
    for i in m.keys():
        m3[m2[i]] = m[i]
    res = sorted(m3.items(), reverse=True)
    
    for r in res:
        print(r[1])
        if len(r[1]) == 1:
            answer.append(r[1][0][1])
            continue
        tmp = sorted(r[1], reverse = True)
        top_list = []
        top = tmp[0][0]
        for t in tmp:
            if t[0] == top:
                top_list.append(t[1])
            else: break
        if len(top_list) == 1:
            answer.append(top_list.pop())
            top = tmp[1][0]
            for t in tmp[1:]:
                if t[0] == top:
                    top_list.append(t[1])
                else: break
            answer.append(sorted(top_list)[0])
        else :
            answer += sorted(top_list)[0:2]
    
   
            
    return answer

print(solution(['A','A','B','A'],[5, 5, 6, 5]))