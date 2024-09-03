import numpy as np

def suit_np(rows,cols):
    toRet=np.zeros([rows,cols])
    for i in range(rows):
        for j in range(cols):
            toRet[i][j]=i
    return toRet