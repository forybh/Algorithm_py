
import math

def is_prime(num):
    if num == 1: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False 
    return True

def solution(n, k):
    answer = 0
    num = ''
    while n > 0 :
        num += str(n%k)
        n //= k
    
    num = num[::-1]
    temp = num.split('0')
    for t in temp:
        if t == '': continue
        if is_prime(int(t)):
            answer += 1
            
    return answer

print(solution(1000000, 10))