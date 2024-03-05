def solution(record):
    answer = []
    dict={}
    for i in record:
        if i.split(' ')[0]=='Enter' or i.split(' ')[0]=='Change':
            key=i.split(' ')[1]
            value=i.split(' ')[2]
            dict[key]=value
    for i in record:
        if i.split(' ')[0]=='Enter':
            key=i.split(' ')[1]
            answer.append(dict[key]+'님이 들어왔습니다.')
        elif i.split(' ')[0]=='Leave':
            key=i.split(' ')[1]
            answer.append(dict[key]+'님이 나갔습니다.')
    # print(dict)   
    return answer