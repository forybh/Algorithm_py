N, M = map(int, input().split())
board = [list(map(int, input().split())) for x in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0
board_flag = True
for i in range(M):
    d, s = map(int, input().split())
    d -= 1
    break_x = N//2
    break_y = N//2
    for j in range(1, s+1):
        break_x += directions[d][1]
        break_y += directions[d][0]
        board[break_y][break_x] = -1
    print("board : ", board)
    # board를 1차원 배열로 바꿔야함
    cur = [N // 2, N // 2]
    directions2 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    marbles = []
    direction = 0
    cnt = 1
    two = 0
    flag = False
    while True:
        for i in range(1, cnt + 1):
            cur[1] += directions2[direction][1]
            cur[0] += directions2[direction][0]
            if not (0 <= cur[0] < N and 0 <= cur[1] < N):
                flag = True
                break
            if board[cur[0]][cur[1]] == 0:
                flag = True
                break
            if board[cur[0]][cur[1]] == -1:
                continue
            marbles.append(board[cur[0]][cur[1]])
        if flag:
            break
        direction = (direction + 1) % 4
        two += 1
        if two == 2:
            two = 0
            cnt += 1
    print("marbles : ", marbles)
    if len(marbles) == 0:
        break
    marble = 0
    cnt = 1
    while True:
        flag = True
        for idx in range(len(marbles)):
            if marbles[idx] == marble: #연속
                cnt += 1
            else: #불연속
                if cnt > 3: # 폭발
                    flag = False
                    marble = marbles[idx]
                    for _ in range(cnt):
                        print(idx, cnt)
                        marbles.pop(idx - cnt)
                    answer += marble * cnt
                    print(marble, cnt)
                    print(marble * cnt)
                    cnt = 1
                    break
                cnt = 1
                marble = marbles[idx]
        if flag:
            break
    marble = marbles[0]
    cnt = 1
    new_marbles = []
    for i in range(1, len(marbles)):
        if marbles[i] == marble: #연속
            cnt += 1
        else: # 불연속 개수, 번호
            new_marbles.append(cnt)
            new_marbles.append(marble)
            marble = marbles[i]
            cnt = 1
        if i == len(marbles)- 1:
            new_marbles.append(cnt)
            new_marbles.append(marble)

    new_board = [[0] * N for _ in range(N)]
    marble_index = 0

    cur = [N // 2, N // 2]
    direction = 0
    cnt = 1
    two = 0
    flag = False
    print("new_marbles : ", new_marbles)
    while True:
        for i in range(1, cnt + 1):
            cur_marble = new_marbles[marble_index]
            cur[1] += directions2[direction][1]
            cur[0] += directions2[direction][0]
            if not (0 <= cur[0] < N and 0 <= cur[1] < N):
                flag = True
                break
            new_board[cur[1]][cur[0]] = cur_marble
            marble_index += 1
            if marble_index >= len(new_marbles):
                flag = True
                break
        if flag:
            break
        direction = (direction + 1) % 4
        two += 1
        if two == 2:
            two = 0
            cnt += 1
    print("new_board : ", new_board)
    board = new_board

print(answer)
