

def solution(n, results):
    answer = 0
    pm = [[0 for x in range(n+1)] for y in range(n+1)]
    for r in results:
        pm[r[0]][r[1]]= 1
        
    for i in range(1,n+1):
        for j in range(1, n+1):
            for k in range(1, n+1): 
                if(pm[j][i]== 1 and pm[i][k] == 1): 
                    pm[j][k] = 1
    print(pm)
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if pm[i][j] == 1 or pm[j][i] == 1:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))