def solution(maps):
    answer = 0
    # 우, 아래, 좌, 위 
    dir_x = [1, 0, -1, 0]
    dir_y = [0, 1, 0, -1]
    start = []
    for i in range(maps):
        for j in range(maps[0]):
            if maps[i][j] != '.':
                start = [i, j, maps[i][j]]
                break
        if len(start) != 0:
            break
    
    areas = [[start]]
    
 
        
    return answer