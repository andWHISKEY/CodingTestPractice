def solution(s):
    answer=s.split(' ')
    new=''
    for x,i in enumerate(answer):
        answer[x]=i.capitalize()
    for i in answer:
        new+=i+' '
                
    return new[:-1]
