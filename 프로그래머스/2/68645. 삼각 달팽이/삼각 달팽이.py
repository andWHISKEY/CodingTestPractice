def triangle(n,num,x,y,arr):
    #중단점
    if n<0:
        return arr
    elif n-1==0:
        arr[x][y]=num
        return arr
    #하향
    for i in range(n-1):
        arr[x][y]=num
        x+=1
        num+=1
    #우향
    for i in range(n-1):
        arr[x][y]=num
        y+=1
        num+=1    
    #대각선
    for i in range(n-1):
        arr[x][y]=num
        x-=1
        y-=1
        num+=1
    x+=2
    y+=1
    #dp
    triangle(n-3,num,x,y,arr)
    
    
def solution(n):
    N=n
    result=[]
    arr=[[0]*n for i in range(n)]
    triangle(N,1,0,0,arr)
    arr=sum(arr,[])
    for x in arr:
        if x>0:
            result.append(x)
    return result