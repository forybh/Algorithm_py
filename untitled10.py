def solution(N, M, K):
    answer = 0
    data = list(map(int, input().split()))
    print(data)
    data.sort(reverse=True)
    print(data)
    count = 0
    for x in data:
        for i in range(K):
            answer += data[0]
            count += 1
            print(answer, count)
            if count == M:
                return answer
        answer += data[1]
        count += 1
        print(answer, count)
        if count == M:
            return answer
        
        
        

print(solution(5,8,3))
        