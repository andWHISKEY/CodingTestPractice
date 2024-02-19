def solution(n, times):
    answer = 0
    start=1
    end=max(times)*n
    # 이분탐색이니 start가 end 이하인 동안
    while start<=end:
        mid=(start+end)//2
        #심사한 사람 수
        people=0
        
        for time in times:
            #해당 심사대에 주어진 시간동안 심사 받은 수 더하기
            people+=mid//time
            # print(mid,time,mid//time,'people:',people,'n:',n)
            #중간에라도 이미 n명 이상 심사한 경우 break
            if people>=n:
                break
        #n명초과 혹은 정확히 맞아 떨어지면 시간 넉넉하단 거니까
        if people>=n:
            answer=mid
            end=mid-1
            # print('시간많아')
        #n명 미만 시간 부족
        else:
            # print('시간부족')
            start=mid+1
    return answer