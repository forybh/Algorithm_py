import heapq
import copy

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num, count = input().split()
    num =list(map(int, list(num)))
    count = int(count)
    
    numSet = list(set(num))
    pq = []
    for n in numSet:
        heapq.heappush(pq, -n)
    
    best = sorted(num, reverse = True)
    cnt = 0
    q = [(num, 0)]
    answer = []
    m = -pq[0]
    while len(q) != 0:
        top_num, top_cnt = q.pop(0)
        
        if top_cnt == count:
            answer.append(top_num)
            continue
        ttt = 0
        if len(pq) == 0 :
            for i in range(num):
                if i == m:
                    ttt += 1
                if ttt > 1:
                    break
            if ttt > 1:
                answer.append(top_num)
            else:
                tmp = top_num[-2]
                top_num[-2] = top_num[-1]
                top_num[-1] = tmp
                q.append((top_num, top_cnt+1))
            continue
        m = -pq[0]
        
            
        tmp = [] # 가장 큰 수인 것들 위치
        for idx,n in enumerate(reversed(top_num)):
            if n == m:
                tmp.append(len(num)- 1 -idx)
        
        tmp_cnt = 0
        print(m, tmp)
        for i in range(len(num)):
            if top_num[i] < m: #정답 후보
                temp = top_num[i]
                for t in tmp:
                    if i < t: # 교환
                        tmp_cnt += 1
                        temp_num = copy.deepcopy(top_num)
                        temp_num[t] = temp
                        temp_num[i] = m
                        q.append((temp_num, top_cnt + 1))
                break
        if tmp_cnt == 0:
            heapq.heappop(pq)
            q.append(((top_num, top_cnt)))
    answer.sort(reverse=True)
    best_answer = ''
    for a in answer[0]:
        best_answer += str(a)
    print(f"#{test_case} {best_answer}")
            
            
                
        
            
        
        
            
            
        
            
        
        
            
        
    #1. 가장 큰수가 맨 앞으로 오게
    #2. 만약 가장 큰 수가 여러개면 여러개중에 가장 끝에 있는애 가져오기
    #3. 만약 이미 가장 큰 수가 되었다면 가장 오른쪽 애 둘이 바꾸기

