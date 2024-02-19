def dfs_recursive(numbers,target,idx,values):
    global cnt
    
    if (idx==len(numbers)) & (values==target):
        cnt+=1
        return
    elif idx==len(numbers):
        return
    
    dfs_recursive(numbers,target,idx+1,values+numbers[idx])
    dfs_recursive(numbers,target,idx+1,values-numbers[idx])
    

def solution(numbers, target):
    global cnt
    cnt=0
    
    dfs_recursive(numbers,target,0,0)
    return cnt