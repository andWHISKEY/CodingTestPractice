def solution(s):
    length=len(s)
    i=1
    count=1
    min_len=length
    past_sentence=""
    answer=""
    while(i<=length/2):
        for x in range(0,length,i):
            if x+i>length:
                sentence=s[x:]
            else:
                sentence=s[x:x+i]
                
            if sentence==past_sentence:
                count+=1
            else:
                if count!=1:
                    answer+=(str(count)+past_sentence)
                else:
                    answer+=past_sentence
                count=1
            past_sentence=sentence
        if count!=1:
            answer+=(str(count)+past_sentence)
        else:
            answer+=past_sentence    
        i+=1
        count=1
        min_len=min(min_len,len(answer))
        # print(i-1,answer,len(answer),min_len)
        past_sentence=""
        answer=""
        
    return min_len