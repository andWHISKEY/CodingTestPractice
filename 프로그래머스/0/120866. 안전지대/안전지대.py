import numpy as np
import copy

def solution(board):
    length=len(board)
    board2=copy.deepcopy(board)
    for idx,i in enumerate(board):
        for jdx,j in enumerate(board[idx]):
            if j==1:
                try:
                    if idx+1<length:
                        board2[idx+1][jdx]=1
                except:
                    pass
                try:
                    if idx-1>=0:
                        board2[idx-1][jdx]=1
                except:
                    pass
                try:
                    if jdx+1<length:
                        board2[idx][jdx+1]=1
                except:
                    pass
                try:
                    if jdx-1>=0:
                        board2[idx][jdx-1]=1
                except:
                    pass
                try:
                    if idx+1<length and jdx+1<length:
                        board2[idx+1][jdx+1]=1
                except:
                    pass
                try:
                    if idx+1<length and jdx-1>=0:
                        board2[idx+1][jdx-1]=1
                except:
                    pass
                try:
                    if jdx+1<length and idx-1>=0:
                        board2[idx-1][jdx+1]=1
                except:
                    pass
                try:
                    if idx-1>=0 and jdx-1>=0:
                        board2[idx-1][jdx-1]=1
                except:
                    pass
    board2=np.array(board2)
    # print(board2)
    unique,count=np.unique(board2,return_counts=True)
    # print(unique,count,type(unique[0]))
    if int(unique[0])==0:
        return int(count[0])
    return 0

