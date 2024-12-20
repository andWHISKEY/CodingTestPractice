def solution(numbers):
    
    numbers = sorted([str(n) for n in numbers], key = lambda x : x*3, reverse = True)
    # print(numbers)
    answer=''.join(numbers)
    while len(answer)>=1 and answer[0]=='0':
        answer=answer[1:]
    
    if len(answer)==0:
        return "0"    
    
    return answer