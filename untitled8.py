import collections
def solution(id_list, report, k):
    answer = []
    cnt_dict = collections.defaultdict(int)
    ban_dict = collections.defaultdict(set)
    for re in report: 
        f, t = re.split() #누가 누구를
        ban_dict[f].add(t)
    
    for key in ban_dict.keys():
        for s in ban_dict[key]:
            cnt_dict[s] += 1
    
    ban_list = set()
    for key in cnt_dict:
        if cnt_dict[key] >= k :
            ban_list.add(key)
    
    for i in id_list:
        cnt = 0
        for j in ban_dict[i]:
            if j in ban_list:
                cnt += 1
        answer.append(cnt)
        
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))