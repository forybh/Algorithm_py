import copy
def solution(n, info):
    answer = []
    apeach_score = 0
    for i in range(11):
        if info[i] != 0:
            apeach_score += (10-i)
    
    queue = [[n, 0,-apeach_score,[0,0,0,0,0,0,0,0,0,0,0]]] #남은 화살, 지금 쏠 점수, 점수 차이
    
    tmp_list = []
    while len(queue) != 0:
        top = queue.pop(0)
        if top[0] < 0 or top[1] >= 10:
            if top[2] > 0:
                tmp_list.append(top)
            continue
        if top[0] > info[top[1]]: #맞출 수 있을때
            if info[top[1]] == 0: # 어피치가 안맞춘 과녘일때
                tm_l = copy.deepcopy(top[3])
                queue.append([top[0], top[1]+1, top[2], tm_l]) # 안맞출때
                tm_l2 = copy.deepcopy(top[3])
                tm_l2[top[1]] = 1
                queue.append([top[0]-1, top[1]+1, top[2] + (10-top[1]), tm_l2]) # 맞출 때
    
            else: #어피치가 맞춘 과녁일때
                tm_l = copy.deepcopy(top[3])
                remain = top[0] - info[top[1]] - 1
                score = top[2] + 2*(10 - top[1])
                
                queue.append([top[0], top[1]+1, top[2], tm_l]) # 안맞출때
                tm_l2 = copy.deepcopy(top[3])
         
                tm_l2[top[1]] = info[top[1]] + 1
    
                queue.append([remain, top[1]+1, score, tm_l2]) # 맞출 때
                
        else:
            tm_l = copy.deepcopy(top[3])
            queue.append([top[0], top[1]+1, top[2], tm_l]) # 안맞출때
            
    if len(tmp_list) == 0:
        return [-1]
    
    tmp_list.sort(key = lambda x: -x[2])
    max_gap = tmp_list[0][2]
    tmp_list2 = []
    
    for tmp in tmp_list:
        if tmp[0] !=0:
            tmp[3][10] = tmp[0]
        if tmp[2] == max_gap:
            tmp_list2.append(tmp[3])
    
    if len(tmp_list2) == 1:
        answer = tmp_list2[0]
    else:
        tmp_list2.sort(key = lambda x: (-x[10],-x[9],-x[8],-x[7],-x[6],-x[5],-x[4],-x[3],-x[2],-x[1],-x[0]))
        answer = tmp_list2[0]

    
    return answer