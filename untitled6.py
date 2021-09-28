def solution(board, skill):
    answer = 0
    for s in skill:
        if s[0] == 1:
            for i in range(s[2], s[4]+1):
                for j in range(s[1], s[3]+1):
                    board[j][i] -= s[5]
        if s[0] == 2:
            for i in range(s[2], s[4]+1):
                for j in range(s[1], s[3]+1):
                    board[j][i] += s[5]

    answer = decompose(board, (len(board), len(board[0])), 0, 0)
    
    return answer


def decompose(board, n, y, x):
    res = 0
    
    if n[0] == 1:
        cnt = 0
        for i in range(x, x+n[1]):
            if board[y][i] > 0:
                cnt += 1
        return cnt
    elif n[1] == 1:
        cnt = 0
        for i in range(y, y+n[0]):
            if board[i][x] > 0:
                cnt += 1
        return cnt
        
    flag = True
    for i in range(y, y+n[0]):
        if not flag:
            break
        for j in range(x, x+n[1]):
            if board[i][j] <= 0:
                flag = False
                break
            
    if flag:
        return n[0] * n[1]
 
    else:
        decreased_n1 = n[0] // 2
        decreased_n2 = n[1] // 2
        if n[0] % 2 == 1 and n[1] % 2 == 1:
             
            res += decompose(board,(decreased_n1, decreased_n2), y, x)
            res += decompose(board,(decreased_n1, decreased_n2+1), y, x+decreased_n2)
            res += decompose(board,(decreased_n1+1, decreased_n2), y+decreased_n1, x)
            res += decompose(board,(decreased_n1+1, decreased_n2+1), y+decreased_n1, x+decreased_n2)
        elif n[1] % 2 == 1:
             
            res += decompose(board,(decreased_n1, decreased_n2), y, x)
            res += decompose(board,(decreased_n1, decreased_n2+1), y, x+decreased_n2)
            res += decompose(board,(decreased_n1, decreased_n2), y+decreased_n1, x)
            res += decompose(board,(decreased_n1, decreased_n2+1), y+decreased_n1, x+decreased_n2)
        elif n[0] % 2 == 1:
                 
            res += decompose(board,(decreased_n1, decreased_n2), y, x)
            res += decompose(board,(decreased_n1, decreased_n2), y, x+decreased_n2)
            res += decompose(board,(decreased_n1+1, decreased_n2), y+decreased_n1, x)
            res += decompose(board,(decreased_n1+1, decreased_n2), y+decreased_n1, x+decreased_n2)
        else:
            res += decompose(board,(decreased_n1, decreased_n2), y, x)
            res += decompose(board,(decreased_n1, decreased_n2), y, x+decreased_n2)
            res += decompose(board,(decreased_n1, decreased_n2), y+decreased_n1, x)
            res += decompose(board,(decreased_n1, decreased_n2), y+decreased_n1, x+decreased_n2)
  
    return res
    

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
         [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))