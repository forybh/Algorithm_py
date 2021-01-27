def solution(progresses, speeds):
    
    answer = []
 
    while progresses:
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            while progresses[0] >= 100:
                progresses.pop(0)    
                count += 1
                if not progresses:
                    break
        if count > 0:
            answer.append(count)
        print(progresses)
            
    return answer

print(solution([93, 30, 55], [1, 30, 5]))