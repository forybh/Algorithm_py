import copy
N, M = map(int, input().split())
cctv = []
room = []

ans = 0

for i in range(N):
    tmp = list(map(int,input().split()))
    for j, t in enumerate(tmp):
        if t != 0 and t != 6:
            cctv.append((t, i, j))
    room.append(tmp)


def findZero(m):
    res = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 0:
                res += 1
    return res

def findUp(m, y, x):
    s = y - 1
    while s >= 0 :
        if m[s][x] == 6:
            break
        m[s][x] = -1
        s -= 1

    return m

def findDown(m, y, x):
    s = y + 1
    while s < N:
        if m[s][x] == 6 :
            break
        m[s][x] = -1
        s += 1
    return m
    
def findLeft(m, y, x):
    s = x - 1
    while s >= 0 :
        if m[y][s] == 6 :
            break
        m[y][s] = -1
        s -= 1
    return m
    
def findRight(m, y, x):
    s = x + 1
    while s < M:
        if m[y][s] == 6 :
            break
        m[y][s] = -1
        s += 1
    return m

def solution(m, cc):
    q = [m]
    ans = 100
    for c in cc:
        tmpq = []
        while len(q) > 0:
            ma = q.pop(0)
            m1 = copy.deepcopy(ma)
            m2 = copy.deepcopy(ma)
            m3 = copy.deepcopy(ma)
            m4 = copy.deepcopy(ma)
            if c[0] == 1:
                tmpq. append(findUp(m1, c[1], c[2]))
                tmpq. append(findDown(m2, c[1], c[2]))
                tmpq. append(findLeft(m3, c[1], c[2]))
                tmpq. append(findRight(m4, c[1], c[2]))
            if c[0] == 2:
                tmpq.append(findRight(findLeft(m1, c[1], c[2]), c[1], c[2]))
                tmpq.append(findUp(findDown(m2, c[1], c[2]), c[1], c[2]))
                         
            if c[0] == 3:
                tmpq.append(findRight(findUp(m1, c[1], c[2]), c[1], c[2]))
                tmpq.append(findLeft(findDown(m2, c[1], c[2]), c[1], c[2]))
                tmpq.append(findRight(findDown(m3, c[1], c[2]), c[1], c[2]))
                tmpq.append(findLeft(findUp(m4, c[1], c[2]), c[1], c[2]))        
            if c[0] == 4:
                tmpq.append(findLeft(findRight(findUp(m1, c[1], c[2]), c[1], c[2]),c[1],c[2]))
                tmpq.append(findUp(findRight(findDown(m2, c[1], c[2]), c[1], c[2]),c[1],c[2]))
                tmpq.append(findRight(findDown(findLeft(m3, c[1], c[2]), c[1], c[2]),c[1],c[2]))
                tmpq.append(findUp(findDown(findLeft(m4, c[1], c[2]), c[1], c[2]),c[1],c[2]))
                
            if c[0] == 5:
                tmpq.append(findDown(findLeft(findRight(findUp(m1, c[1], c[2]), c[1], c[2]),c[1],c[2]),c[1],c[2]))
        q = tmpq.copy()
    for r in q:
        ans = min(findZero(r), ans)
    return ans

print(solution(room, cctv))
        
    
    
    
    
    
