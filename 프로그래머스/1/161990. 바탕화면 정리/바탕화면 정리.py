import numpy as np

def solution(wallpaper):
    # wallpaper=np.array(wallpaper)
    # print(len(wallpaper[0]),len(wallpaper))
    for idx,i in enumerate(wallpaper):
        wallpaper[idx]=list(i)
        for jdx,j in enumerate(wallpaper[idx]):
            # print(j)
            if j == '.':
                wallpaper[idx][jdx]=0
            else:
                wallpaper[idx][jdx]=1
    
    wallpaper=np.array(wallpaper)
    # print(wallpaper)
    loc = np.where(wallpaper==1)
    # print(loc)
    return [int(min(loc[0])),int(min(loc[1])),int(max(loc[0])+1),int(max(loc[1])+1)]
    # a,b=list(map(list,*wallpaper))
    # print(a)
    # print(b)
    
    # print(wallpaper)
    # answer = []
    # return answer
