import numpy as np
from scipy.cluster.vq import kmeans2
import json

# sig=np.array([1,1,2,3,3,1,5,6,7,8,9,8,7,8,8,7,7,8,9]).astype(float)

def highPass (sig, win_len):
    n = len(sig)
    new_sig = np.zeros( n, dtype = "<f")
     
    for i in range(n - win_len):
        new_sig[i] = sig[i : i+win_len].sum() / win_len

    new_sig[-win_len :] = sig[-win_len :].sum() / win_len

 
    return new_sig

def highPassCeil (sig, win_len):
    n = len(sig)
    new_sig = np.zeros( n, dtype = "<f")
     
    for i in range(n - win_len):
        new_sig[i] = sig[i : i+win_len].sum() // win_len

    new_sig[-win_len :] = sig[-win_len :].sum() // win_len

 
    return new_sig

# def partition(sig, treshold, skip=treshold/2):
#     n = len(sig)

#     start = sig[0]
#     for i in range(0, n, skip):
#         if abs(sig[i] - treshold) > start

def canny(sig):
    n = len(sig)
    new_sig = np.zeros( n, dtype = "<f")
    for i in range(1,n-2):
        new_sig[i] = sig[i-1] * -1/2 + sig[i+1] * 1/2
    return new_sig


def std(sig, N):
    n = len(sig)
    new_sig = np.zeros( n, dtype = "<f")
    for i in range(1,n-N-1):
        new_sig[i] = np.std(sig[i : i+N])
    return new_sig


# hp = highPass(sig, 5)
# # p = partition(hp, 4, 3)
# # np.array([1, 1, 1, 5, 6, 111, 122, 999, 1002]).astype(float)
# # json.dumps(hp.tolist())

# # Set the data
# with open('txt.txt', "r") as f:
#     content = f.readlines()

# a = np.array([float(i) for i in content])
# f = highPass(a, 50)
# groups = kmeans2(f, 3)[1]
# # print(json.dumps(groups.tolist()))


# # print(json.dumps(res.tolist()))
# with open('groups.txt', 'w+') as f:
#     for i in groups:
#         f.write(str(i)+'\n')
