def solution(lines):
    answer = 0

    start_list = []
    end_list = []
    for line in lines:
        date, time, pro = line.split()
        pro = int(float(pro[:-1]) * 1000)
        h, m, sec = time.split(":")
        h = int(h) * 3600
        m = int(m) * 60
        s, ms = list(map(int,sec.split(".")))
        end_time = (h + m + s)*1000 + ms
        start_time = end_time - pro + 1
        start_list.append(start_time)
        end_list.append(end_time)
        
    for i in range(len(start_list)):
        s1 = start_list[i]
        e1 = end_list[i]
        count = 1
        for j in range(i+1,len(start_list)):
            if i == j: continue
            s2 = start_list[j]
            e2 = end_list[j]
            if e1 > s2 -1000 :
                count += 1
        answer = max(count, answer)
    return answer