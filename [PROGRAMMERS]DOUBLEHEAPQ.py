import heapq

def solution(operations):
    answer = []
    hq1 = []
    hq2 = []
    length = 0
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == 'I':
            length += 1
            heapq.heappush(hq1, num)
            heapq.heappush(hq2, -num)
        else:
            if length == 0:
                hq1.clear()
                hq2.clear()
                continue
            length -= 1
            if num == 1:
                heapq.heappop(hq2)
                    
            else:
                heapq.heappop(hq1)
                
            if length == 0:
                hq1.clear()
                hq2.clear()

                
            
    if length == 0:
        answer = [0,0]
    else:
        answer = [-heapq.heappop(hq2), heapq.heappop(hq1)]
        
    return answer

#[6,5]
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))

