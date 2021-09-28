import collections

def solution(fees, records):
    answer = []
    record_dict = collections.defaultdict(list)
    for record in records:
        time, numer, inout = record.split()
        h, m = time.split(":")
        toMinute = int(h) * 60 + int(m)
        record_dict[numer].append(toMinute)

    fee_list = []
    for k in record_dict.keys():
        use_time = 0
        if len(record_dict[k]) % 2 == 1:
            record_dict[k].append(60*23 + 59)
        for i in range(0, len(record_dict[k]), 2): # 출 입 기록 조회
            use_time += record_dict[k][i+1] - record_dict[k][i]
    
        if use_time <= fees[0]:
            fee = fees[1]
        else:
            over_time = use_time - fees[0]
            if over_time % fees[2] == 0:
                over_fee = (over_time//fees[2]) * fees[3]
            else:
                over_fee = (over_time//fees[2] + 1) * fees[3]
            fee = fees[1] + over_fee
        fee_list.append((fee,k))
    fee_list.sort(key = lambda x: x[1])
    for f in fee_list:
        answer.append(f[0])
            
    
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))