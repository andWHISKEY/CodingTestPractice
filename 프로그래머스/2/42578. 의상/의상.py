from collections import Counter

def solution(clothes):
    temp=list(map(list,zip(*clothes)))
    print(temp)
    dic=Counter(temp[1])
    print(dic)
    sum=1
    for i in list(dic.values()):
        sum*=(i+1)

    return sum-1