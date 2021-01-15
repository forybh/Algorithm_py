def solution(array, commands):
    answer = [0 for _ in range((len(commands)))]
     
    for idx, c in enumerate(commands):
        temp_list = array[c[0]-1:c[1]]
        answer[idx] = (sorted(temp_list)[c[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))