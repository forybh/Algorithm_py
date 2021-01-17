from collections import deque

def solution(people, limit):
    answer = len(people) 
    people.sort()
    deq = deque(people)
    
    while len(deq)>1:
        if deq[0] + deq[-1] <= limit:
           deq.popleft()
           deq.pop()
           answer -= 1
        else:
            deq.pop()
        
    return answer

