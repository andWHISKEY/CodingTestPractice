def solution(answers):
    N=len(answers)
    
    ppls=[[1,2,3,4,5],
       [2,1,2,3,2,4,2,5],
       [3,3,1,1,2,2,4,4,5,5]]
    
    answer = [[1,0],[2,0],[3,0]]
    max_cnt=0
    
    for pdx,ppl in enumerate(ppls):
        pN=len(ppl)
        ppls[pdx]=ppl*(N//pN) + ppl[:N%pN]
    
    for idx,i in enumerate(answers):
        for j in range(3):
            if i==ppls[j][idx]:
                answer[j][1]+=1
            if max_cnt<answer[j][1]:
                max_cnt=answer[j][1]
                
    answer.sort(key=lambda x: (-x[1], x[0]))
    
    final_answer=[]
    for i in answer:
        if i[1]==max_cnt:
            final_answer.append(i[0])
    
    return final_answer