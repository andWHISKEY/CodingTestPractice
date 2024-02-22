def solution(s):
    answer = True
    temp=[]
    for i in s:
        if len(temp)==0 and i==')':
            return False
        elif i=='(':
            temp.append(0)
        elif i==')':
            # try:
            temp.pop()
            # except IndexError:
            #     return False
            
    
    return len(temp)==0