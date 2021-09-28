import copy
from collections import deque

N, L, R = map(int, input().split())
A = []

for i in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = 0
while True: 
    copyA = copy.deepcopy(A)
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 1:
                continue
            visited[y][x] = 1
            q = deque()
            q.append([y,x])
            l = [(y,x)]
            cnt = 1
            popul = A[y][x]
            while q:
                top = q.popleft()
                
                for i in range(4): #네 방향 탐색
                    nx = top[1] + dx[i]
                    ny = top[0] + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: #범위 벗어남
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    gap = abs(A[top[0]][top[1]] - A[ny][nx])
                    if L <= gap <= R: # 조건 만족
                        visited[ny][nx] = 1
                        q.append((ny, nx))
                        l.append((ny, nx))
                        cnt += 1
                        popul += A[ny][nx]
            divi = popul // cnt
            for contry in l:
                A[contry[0]][contry[1]] = divi
    if copyA == A:
        break
    else:
        answer += 1

print(answer)
      
                
                    
                
                
            
    



        
    



        

