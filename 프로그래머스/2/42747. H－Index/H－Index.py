def solution(citations):
    n=len(citations)
    citations.sort(reverse=True)
    for i in range(n,0,-1):
        try: 
            if citations[i-1]>=i:
                return i
        except:
            pass
    return 0
    # answer = 0
    # return answer