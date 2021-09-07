def solution(relation):
    answer = 0
    for i in range(len(relation[0])): #첫번째 기준점
        print(i)
        one = set()
        for r in relation:
            one.add(r[i])
        if len(one) == len(relation):
            answer += 1
            #continue
        
        for j in range(i + 1, len(relation[0])): #두번째 기준점
            print(i, j)
            two = []
            for r in relation:
                if (r[i],r[j]) in two:
                    break
                two.append((r[i],r[j]))
            if len(two) == len(relation):
                answer += 1
                #continue
                
            for k in range(j+1, len(relation[0])):
                l = []
                print(i, j, k)
                for rel in relation:
                    tmp = []
                    tmp.append(rel[i])
                    for t in range(j, k+1):
                        tmp.append(rel[t])
                    if tmp in l:
                        break
                    else:
                        l.append(tmp)
                if len(l) == len(relation):
                    answer += 1
                    #break
    
               
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))