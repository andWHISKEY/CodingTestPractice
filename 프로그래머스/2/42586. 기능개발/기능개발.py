import math

def solution(progresses, speeds):
    timetable=[]
    answer=[]
    for x,y in zip(progresses,speeds):
        timetable.append(math.ceil((100-x)/y))
    print(timetable)  
    cnt=1
    answer_num=timetable[0]
    for i in timetable[1:]:
        if i>answer_num:
            answer.append(cnt)
            answer_num=i
            cnt=1
        else:
            cnt+=1
    answer.append(cnt)        
    return answer       
            
    










# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             print(Q)
#             Q.append([-((p-100)//s),1])
#         else:
#             print(Q)
#             Q[-1][1]+=1
#     return [q[1] for q in Q]

# def solution(progresses, speeds):
#     answer = []
#     temp=[]
#     temp2=0
#     for idx,i in enumerate(progresses):
#         temp.append(math.ceil((100-progresses[idx])/speeds[idx]))
    
#     for idx,i in enumerate(temp):
#         if idx==0:
#             temp2=i
#             cnt=1
#         else:
#             if i<=temp2:
#                 cnt+=1
#             else:
#                 answer.append(cnt)
#                 cnt=1
#                 temp2=i
    
#     answer.append(cnt)
    
#     return answer