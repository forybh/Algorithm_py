from itertools import combinations
def solution(relation):
    def checkCandidate (colLst, rows):
            tmp = [tuple([item[idx] for idx in colLst]) for item in relation]
            if len(set(tmp)) != rows:
                    return False
            else: return True
            
    rows = len(relation)
    cols = len(relation[0])
    colLst = range(cols)
    lst = []
    for leng in range(1, cols+1):
        comb = combinations(colLst,leng)
        for n1 in list(comb):
            if checkCandidate (n1, rows):
                lst.append(set(n1))
    for el1 in lst[:]:
        for el2 in lst[:]:
            if el1 == el1 & el2:
                if el1 != el2:
                    lst.remove(el2)
    return len(lst)
