from heapq import heappush, heappop, heapify

def solution(jobs):
    answer=0 #걸린시간
    now=0 #현재시간
    i=0 #처리일갯수
    
    start=-1	
    heap=[]
    
    while i<len(jobs):
        for j in jobs:
            if start<j[0]<= now:
                heappush(heap,[j[1],j[0]])
        
        if len(heap)>0: #처리할 일 있는 경우 
            cur=heappop(heap)
            start=now	
            now+=cur[0]	#현재시간 갱신
            answer+=now-cur[1] #처리시간 더해주기
            i+=1 
            
        else: 
            now+=1
    return answer//i