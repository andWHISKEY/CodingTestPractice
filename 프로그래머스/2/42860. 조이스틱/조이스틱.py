def solution(name):
    answer=0
    A_cnt=0
    min_move=len(name)-1
    for idx,i in enumerate(name):
        answer+=min(ord(i)-ord('A'),ord('Z')+1-ord(i))
        flag=idx+1
        while(flag<len(name) and name[flag]=='A'):
            flag+=1
        
        min_move=min(min_move,idx*2+len(name)-flag, 2*(len(name)-(flag))+idx)
    answer+=min_move
    
    return answer

