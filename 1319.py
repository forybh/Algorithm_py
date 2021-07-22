def solution():
    N = int(input())
    find = int(input())
    
    x_dir = [0,1,0,-1]
    y_dir = [-1,0,1,0]
    x_cur = N//2
    y_cur = N//2
    cur_dir = 0
    
    answer = [[0]*N for _ in range(N)] 
    count = 0
    length = 1
    cur_N = 1
    while True:
        for _ in range(length):
            if cur_N > N**2:
                break
                
            answer[y_cur][x_cur] = cur_N
            cur_N += 1
            y_cur += y_dir[cur_dir]
            x_cur += x_dir[cur_dir]
            
        if cur_N > N**2:
            break
        count += 1
        if count == 2:
            count = 0
            length += 1
        cur_dir += 1
        cur_dir %= 4
    for i, l in enumerate(answer):
        print(" ".join(str(x) for x in l))
        if find in l:
            find_index = (i, l.index(find))
    print(" ".join(str(f+1) for f in find_index))

solution()
        
        
        