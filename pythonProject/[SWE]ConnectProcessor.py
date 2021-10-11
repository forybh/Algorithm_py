
# 가장 많이 연결하면서 가장 짧은 선 이용
def dfs(board, index, line, linked):
    global res, max_cnt, cores
    # if linked == max_cnt:
    #     if line >= res: #선이 길거나 같음
    #         return

    if index >= len(cores): # 가장 끝 코어까지 옴
        if linked == max_cnt:
            res = min(res, line)
            print(f"연결된수 {linked} 전선길이{line}")
        elif linked > max_cnt:
            max_cnt = linked
            res = line
        return

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def checkList(board, ny, nx, d):
        flag = True
        l = 0
        while True:
            ny += dy[d]
            nx += dx[d]
            if 0 <= ny < len(board) and 0 <= nx < len(board):
                if board[ny][nx] == 0:
                    l += 1
                else:
                    flag = False
                    break
            else:
                break
        if flag:
            return l
        else:
            return 0

    def fill(board, ny, nx, d):
        while True:
            ny += dy[d]
            nx += dx[d]
            if 0 <= ny < len(board) and 0 <= nx < len(board):
                board[ny][nx] = 1
            else:
                break
    def unFill(board, ny, nx, d):
        while True:
            ny += dy[d]
            nx += dx[d]
            if 0 <= ny < len(board) and 0 <= nx < len(board):
                board[ny][nx] = 0
            else:
                break
    y, x = cores[index]
    flag = True
    for d in range(4):
        cl = checkList(board, y, x, d)
        if cl == 0: #이쪽 방향 안되는 거
            dfs(board, index+1, line, linked)
            flag = False
        else: #이쪽 방향으로 연결 가능
            fill(board,y,x,d)
            dfs(board, index + 1, line + cl, linked + 1)
            unFill(board,y,x,d)

    if flag: # 네 방향 다 안됐을 경우
        dfs(board, index+1, line, linked)

T = int(input())

for test_num in range(1, T+1):
    res = 1e6
    max_cnt = 0
    N = int(input())
    board = []
    cores = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j, te in enumerate(temp):
            if te == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1: # 이미 연결되어 있음
                    continue
                cores.append((i, j))
        board.append(temp)
    print(cores)
    dfs(board,0,0,0)
    print(f"#{test_num} {res}")