def solution(rows, columns, queries):
    arr=[[0 for _ in range (columns)] for _ in range(rows)]
    temp=[]
    answer = []
    num=1
    for i in range(rows):
        for j in range(columns):
            arr[i][j]=num
            num+=1
    # print(arr)
    for x1,y1,x2,y2 in queries:
        x1-=1
        x2-=1
        y1-=1
        y2-=1
        temp=[]
        temp_num=[]
        for i in range(y1,y2):
            temp.append([x1,i])
            temp_num.append(arr[x1][i])
        for i in range(x1,x2):
            temp.append([i,y2])
            temp_num.append(arr[i][y2])
        for i in range(y2,y1,-1):
            temp.append([x2,i])
            temp_num.append(arr[x2][i])
        for i in range(x2,x1,-1):
            temp.append([i,y1])
            temp_num.append(arr[i][y1])
        for cnt in range(-1,len(temp_num)-1):
            arr[temp[cnt+1][0]][temp[cnt+1][1]]=temp_num[cnt]
        # print(temp)
        # print(temp_num)
        answer.append(min(temp_num))    
    return answer