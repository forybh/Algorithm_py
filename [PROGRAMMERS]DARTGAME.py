def solution(dartResult):
    answer = 0
    num = 0
    num_list = []
    for i, c in enumerate(dartResult):
        if c >= '0' and c <= '9':
            if i != 0:
                num_list.append(num)
            num = int(c)
            if dartResult[i-1] == '1':
                num = 10
                num_list.pop()
        if c == 'D':
            num = num ** 2
        if c == 'T':
            num = num ** 3
        if c == '*':
            num *= 2
            if len(num_list) != 0:
                num_list[-1] *= 2
        if c == '#':
            num *= -1
    num_list.append(num)
    answer = sum(num_list)
       
    return answer