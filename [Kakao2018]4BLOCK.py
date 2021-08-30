def recur(board, ans):
    remove = []
    cnt = 0
    y_dir = [0,1,0,1]
    x_dir = [0,0,1,1]
    for y in range(len(board)-1): #지워야 할 부분 찾기
        for x in range(len(board[0])-1):
            flag = 0
            if board[y][x] == "": continue
            for i in range(1,4):
                if board[y][x] == board[y+y_dir[i]][x+x_dir[i]]:
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                remove.append((y,x))
                
    for r in remove: # 지우기
        y, x = r
        for i in range(4):
            if board[y+y_dir[i]][x+x_dir[i]] != "":
                board[y+y_dir[i]][x+x_dir[i]] = ""
                cnt += 1
            
    for x in range(len(board[0])): # 밑으로 채우기
        tmp = []
        for y in reversed(range(len(board))):
            if board[y][x] != "":
                tmp.append(board[y][x])
        i = 0
        for y in reversed(range(len(board))):
            if i < len(tmp):
                board[y][x] = tmp[i]
            else:
                board[y][x] = ""
            i += 1
    if cnt == 0:
        return ans
    else:
        return recur(board, cnt+ans)
            
    
    
def solution(m, n, board):
    answer = 0
    board =list(map(list, board))
    answer = recur(board, 0)
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))