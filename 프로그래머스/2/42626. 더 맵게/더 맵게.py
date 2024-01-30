from heapq import heappush, heappop, heapify 

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while(scoville[0]<K):
        if len(scoville)==1:
            return -1
        else:
            heappush(scoville,heappop(scoville)+2*heappop(scoville))
            answer+=1
    # print(scoville)
    return answer