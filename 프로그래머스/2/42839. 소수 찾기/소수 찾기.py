from itertools import * 

def isDecimal(num):
    if(num <= 1):
        return False 
    #에라토스테네스의 체
    for i in range(2, num):
        if num%i == 0:
            return False    
    return True


def solution(numbers):

    answer=[]
    for i in numbers:
        answer.append(i)
    per_answer=[]
    length=len(answer)
    while(length>1):
        per_answer+=list(permutations(answer,length))
        length-=1
    final_answer=[]
    for i in per_answer:
        final_answer.append(''.join(map(str, i)))
    final_answer+=answer
    final_answer=list(map(int,final_answer))
    final_answer=list(set(final_answer))
    count=0
    for idx,i in enumerate(final_answer):
        if isDecimal(i):
            count+=1
    return count
#2,3,5,7로 나누어졌을 때, 나머지가 있어야한다. 대신 자기자신이면 몫이 1 나머지 0 ㅇㅋ