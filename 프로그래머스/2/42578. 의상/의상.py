from collections import Counter
def solution(clothes):
    # temp=list(map(list,zip(*clothes)))
    # dic=Counter(temp[1])
    dic=Counter([types for name, types in clothes])
    # print(dic)
    sum=1
    for i in list(dic.values()):
        sum*=(i+1)
        
    return sum-1
    