def solution(progresses, speeds):
    length= len(progresses)
    task=[]
    for i in range(length):
        d=(100-progresses[i])//speeds[i]
        r=(100-progresses[i])%speeds[i]
        if r>0:
            d=d+1
        task.append(d)
    # print(task)    
    answer = []
    max_num=task[0]
    cnt=0
    for i in task:
        # print('m,c,i:',max_num,cnt,i)
        if max_num<i:
            answer.append(cnt)
            max_num=i
            cnt=1
        else:
            cnt+=1
        
    answer.append(cnt)
    return answer