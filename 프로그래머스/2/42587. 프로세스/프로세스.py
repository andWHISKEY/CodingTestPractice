from collections import deque
def solution(priorities, location):
    answer=[]
    answerloc=[]
    priorities=deque(priorities)
    locarr=[0 for _ in range(len(priorities))]
    locarr[location]=1
    locarr=deque(locarr)
    while priorities:
        flag=0
        out=priorities.popleft()
        outloc=locarr.popleft()
        for i in priorities:
            if i>out:
                priorities.append(out)
                locarr.append(outloc)
                flag=1
                break
        if flag==0:        
            answer.append(out)
            # print(priorities,answer)
            answerloc.append(outloc)
    return answerloc.index(1)+1