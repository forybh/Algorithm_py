import collections
from itertools import combinations
import copy

# 0 : 빈칸 1: 벽 2: 바이러스
N, M = map(int, input().split())
board = []
birus = collections.defaultdict(set)
biruses = []
empty = 0
answer = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            birus[i * N + j].add((i, j))
            biruses.append((i,j))
        elif tmp[j] == 0:
            empty += 1
    board.append(tmp)

if empty == 0:
    print(answer)


# 여러개중 M개의 바이러스를 활성화 시켜서 전체 빈칸을 바이러스로

else:
    dir_x = [1, 0, -1, 0]
    dir_y = [0, 1, 0, -1]

    time = 0
    while answer == 0:
        time += 1
        if time > (N - 1) * 2:
            answer = -1
            break
        copy_birus = copy.deepcopy(birus)

        for bir in copy_birus: #바이러스 퍼지게 하
            s = copy.deepcopy(birus[bir])
            for b in copy_birus[bir]:
                y, x = s.pop()
                for i in range(4):
                    dy = y + dir_y[i]
                    dx = x + dir_x[i]
                    if 0 <= dx < N and 0 <= dy < N:
                        if board[dy][dx] != 1:  #빈칸일때기
                            if (dy, dx) in birus[bir]:
                                continue
                            birus[bir].add((dy, dx))

        cand = combinations(birus.keys(), M)
        for ca in cand:
            s = []
            for c in ca:
                s.extend(list(birus[c]))
            cnt = len(set(s))
            for bbb in biruses:
                if bbb in set(s):
                    cnt -= 1
            if cnt == empty:
                answer = time
                break

    print(answer)

import copy
from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1e9


def change_array(array, location):  # 바이러스 놓기
    for i, j in location:
        array[i][j] = "*"
    return array


def bfs(array):
    global result
    q = deque()
    count = 0  # 빈칸의 개수
    for i in range(n):
        for j in range(n):
            if array[i][j] == "*":
                q.append((i, j, 0))
            elif array[i][j] == 0:
                count += 1

    while q:
        x, y, cnt = q.popleft()
        if cnt > result:
            return
        if count == 0:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] == 0:
                    array[nx][ny] = -(cnt + 1)
                    q.append((nx, ny, cnt + 1))
                    count -= 1
                elif array[nx][ny] == 2:
                    array[nx][ny] = -(cnt + 1)
                    q.append((nx, ny, cnt + 1))
                elif array[nx][ny] != "*" and array[nx][ny] < -(cnt + 1):
                    array[nx][ny] = -(cnt + 1)
                    q.append((nx, ny, cnt + 1))
                elif array[nx][ny] == "*":
                    array[nx][ny] = -(cnt + 1)
                    q.append((nx, ny, cnt + 1))

    # 모두 바이러스로 바꼈는지 확인
    answer = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                return -1
            elif array[i][j] != "*" and array[i][j] < 0:
                answer = max(answer, abs(array[i][j]))

    result = min(result, answer)


if __name__ == "__main__":
    n, m = map(int, input().split())  # 연구소의 크기, 바이러스의 개수
    array = [list(map(int, input().split())) for _ in range(n)]

    # 바이러스를 놓을 수 있는 위치 탐색
    location = []
    for i in range(n):
        for j in range(n):
            if array[i][j] == 2:
                location.append((i, j))

    # 모든 경우 bfs 탐색
    result = INF
    for data in list(combinations(location, m)):
        arr = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = array[i][j]
        arr = change_array(arr, data)
        bfs(arr)

    # 출력
    if result == INF:
        print(-1)
    else:
        print(result)





