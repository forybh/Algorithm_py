result = []

def trapped(mat, i):
    row = mat[i-1]
    col = [m[i-1] for m in mat]

    mat[i-1] = col
    for pos, _ in enumerate(mat):
        mat[pos][i-1] = row[pos]
    return mat
    

def dfs(mat, traps, start, end, distance, history):

    if start == end:
        print(distance)
        result.append(distance)
        return
    
    
    for pos in mat[start]:
        if (start, pos) in history:
            return
        
        if mat[start][pos] == 0:
            continue
        
        new_distance = distance + mat[start][pos]
        if pos in traps:
            changed_mat = trapped(mat.copy())
        else:
            changed_mat = mat.copy()
        new_hist = history.copy()
        new_hist.append((start, pos))
        
        dfs(changed_mat, traps, pos, end, new_distance, new_hist)
    
    return
    
     


def solution(n, start, end, roads, traps):
    answer = 0
    mat = [[0 for _ in range(n)]]*(n)
    print(mat)

    for road in roads:
        s, e, d = road
        print(s,e,d)
        if mat[s-1][e-1] != 0:
            mat[s-1][e-1] = min(mat[s-1][e-1], d)
        else: mat[s-1][e-1] = d
     
    for i, dest in enumerate(mat[start]):
        dfs(mat, traps, i, end, dest, [])
    
    
    answer = min(result)
    return answer
        
            
        
        
print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))