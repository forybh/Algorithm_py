from collections import deque
import copy

T = int(input())

for test_num in range(T):
    N, K = map(int, input().split())
    board = []
    max_list = []
    max_val = 0
    for i in range(N):
        temp = list(map(int, input().split()))
        temp_max = max(temp)
        if temp_max > max_val:
            max_val = temp_max
            max_list.clear()
            for j, tt in enumerate(temp):
                if tt == max_val:
                    max_list.append((i, j))

        elif temp_max == max_val:
            for j, tt in enumerate(temp):
                if tt == max_val:
                    max_list.append((i,j))
        board.append(temp)

    #(현재 봉우리 크기, 현재 위치, 등산로 길이, K사용 여부)
    q = deque()
    for m in max_list:
        q.append([max_val, m[0], m[1], 1, 1, {m}])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    res = 0

    while q:
        v, y, x, cnt, useK, s = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] < v : #갈 수 있음
                    ns = copy.deepcopy(s)
                    ns.add((ny,nx))
                    q.append([board[ny][nx], ny, nx, cnt+1, useK, ns])
                    res = max(res, cnt + 1)
                else:
                    if useK == 1: # 깎을 수 있음
                        diff = board[ny][nx] - v   #최대한 조금 깎아야 이득
                        if K > diff: # 깎고 갈 수 있음
                            nk = diff + 1
                            if (ny, nx) not in s:
                                ns = copy.deepcopy(s)
                                ns.add((ny, nx))
                                q.append([board[ny][nx] - nk, ny, nx, cnt+1, 0, ns])
                                res = max(res, cnt + 1)

    print(f"#{test_num+1} {res}")












