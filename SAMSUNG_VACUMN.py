#s = input().split('\n')

r, c = map(int, input().split())
#r, c = map(int, s[0].split())


m = [[0]* c for _ in range(r)]

cur = list(map(int, input().split()))
#cur = list(map(int, s[1].split()))


for i in range(r):
    temp = input().split()
    for j in range(c):
        m[i][j] = int(temp[j])
        
    

def cleaner():
    count = 1
    m[cur[0]][cur[1]] = 1
    cir = 0
    while True:    
        if cir == 4:
            cir = 0
            if cur[2] == 0:
                if cur[0] + 1 < r-1:
                    cur[0] += 1
                    continue
                else: break
            elif cur[2] == 1:
                if cur[1] - 1 > 0:
                    cur[1] -= 1
                    continue
                else: break
            elif cur[2] == 2:
                if cur[0] - 1 > 0:
                    cur[0] -= 1
                    continue
                else: break
            else:
                if cur[1] + 1 < c-1:
                    cur[1] += 1
                    continue
                else: break
        
        
        if cur[2] == 0:
            cur[2] = 3
            cir += 1
            if m[cur[0]][cur[1]-1] == 0:
                cur[1] -= 1
                count += 1
                m[cur[0]][cur[1]] = 1
                cir = 0
            else: continue
            
        elif cur[2] == 1:
            cur[2] = 0
            cir += 1
            if m[cur[0]-1][cur[1]] == 0:
                cur[0] -= 1
                count += 1
                m[cur[0]][cur[1]] = 1
                cir = 0
            else: continue
        elif cur[2] == 2:
            cur[2] = 1
            cir += 1
            if m[cur[0]][cur[1]+1] == 0:
                cur[1] += 1
                count += 1
                m[cur[0]][cur[1]] = 1
                cir = 0
            else: continue
        else:
            cur[2] = 2
            cir += 1
            if m[cur[0]+1][cur[1]] == 0:
                cur[0] += 1
                count += 1
                m[cur[0]][cur[1]] = 1
                cir = 0
            else: continue
                        
    print(count)

    
cleaner()
#for i in m:
#    print(i)
    
        
print(cur)
    
        
        
    
                
                
                
        

    

        

        
        


