def solution(n):
    answer = ''    
    while n > 0:
        answer += str(n%3)
        n = (n-1)//3
    answer = answer.replace('0', '4')[::-1] 
    
    return answer


'''
1,2,4,11,12,14,21,22,24,41,42,44, 111, 112, 114, 
1,2,3, 4, 5, 6, 7, 8, 9,10,11,12, 13,  14,   15,
'''                              
print(solution(15))
# 주문 관련 초기화 