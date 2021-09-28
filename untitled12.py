import collections
def findParent(x, parents):
    if parents[x] != x:
        parents[x] = findParent(parents[x], parents)
    return parents[x]

def unionParent(a, b, parents):
    a = findParent(a, parents)
    b = findParent(b, parents)
    
    if a > b:
        parents[b] = a
    else:
        parents[a] = b
        
def solution(maps):
    answer = 0
    lenY = len(maps)
    lenX = len(maps[0])
    alpha = [0]* 26
    parents = [i for i in range(lenY * lenX)]
    dirY = [0, 1, 0, -1]
    dirX = [1, 0, -1, 0]

    for y in range(lenY):
        for x in range(lenX):
            if maps[y][x] == '.':
                continue
            
            for i in range(4):
                dx = x + dirX[i]
                dy = y + dirY[i]
            
                if 0 <= dx < lenX and 0 <= dy < lenY:
                    if maps[dy][dx] == '.':
                        continue
                    cur_idx = lenX * y + x 
                    next_idx = lenX * dy + dx 
                    unionParent(cur_idx, next_idx, parents)
    
    d = collections.defaultdict(list)
    for i, p in enumerate(parents):
        x = i % lenX
        y = i // lenX
        pa = findParent(p, parents)
        if maps[y][x] == '.':
            continue
        d[pa].append(maps[y][x])
    
    
    for k in d.keys():
        cnt = collections.Counter(d[k])
        sorted_cnt = sorted(cnt.items(), reverse = True, key = lambda x : (x[1], x[0]))
        winner, num = sorted_cnt[0]
        winner = ord(winner) - 65
        alpha[winner] += num
        for alph, count in sorted_cnt:
            if count == num : 
                continue
            alpha[winner] += count

        
            
    answer = max(alpha)
 
    return answer

solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"])

#solution(["XY..", "YX..", "..YX", ".AXY"])