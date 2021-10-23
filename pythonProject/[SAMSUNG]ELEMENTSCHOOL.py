from collections import defaultdict
N = int(input())
d = defaultdict(set)
classRoom = [[0 for _ in range(N)] for _ in range(N)]
direction = [(0, 1), (1, 0), (-1 , 0), (0, -1)]

for i in range(N*N):
    tmp = list(map(int, input().split()))
    cur = tmp[0]  # cur = 자리 고르는 학생
    friends = set(tmp[1:])
    d[cur] = friends
    max_blank = 0
    max_friend = 0
    if i == 0:
        classRoom[1][1] = cur
        continue
    yx = [-1, -1]
    first_blank = []
    for y in range(N):
        for x in range(N):

            if classRoom[y][x] != 0:  #빈칸아님
                continue
            if len(first_blank) == 0:
                first_blank = [y, x]
            blank_cnt = 0
            friend_cnt = 0

            for direct in direction: #네 방향 확인
                ny = y + direct[0]
                nx = x + direct[1]
                if 0 <= ny < N and 0 <= nx < N:
                    if classRoom[ny][nx] in friends:
                        friend_cnt += 1
                    elif classRoom[ny][nx] == 0:
                        blank_cnt += 1

            if friend_cnt > max_friend: # 인접한 칸에 친구 제일 많음
                yx = [y, x]
                max_friend = friend_cnt
                max_blank = blank_cnt

            elif friend_cnt == max_friend: # 인접한 칸에 blank 제일 많음
                if blank_cnt > max_blank:
                    yx = [y, x]
                    max_friend = friend_cnt
                    max_blank = blank_cnt
    if yx == [-1, -1]:
        classRoom[first_blank[0]][first_blank[1]] = cur
    else : classRoom[yx[0]][yx[1]] = cur
answer = 0

for y in range(N):
    for x in range(N):
        cnt = 0
        cur = classRoom[y][x]
        for direct in direction:  # 네 방향 확인
            ny = y + direct[0]
            nx = x + direct[1]
            if 0 <= ny < N and 0 <= nx < N:
                if classRoom[ny][nx] in d[cur]:
                    cnt += 1
        if cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)










