# Ying Zhang Project2
# This project use divide and conquer (recursive) and brute force (non-recursive) algorithm in
# Python for calculating the Closest-Pair Problem. This problem calls for finding the two
# closest points in a set of n points.


import ast
import timeit
import math


import sys

import copy
import numpy

import time
from operator import itemgetter

global points


def get_col(arr, col):
    return map(lambda x: x[col], arr)


with open('input3.txt', 'r') as f:
    points = ast.literal_eval(f.read())
    points_list = numpy.array(points)
    P = points_list[:,0]
    Q = points_list[:,1]

# standard Euclidean distance
def SED(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def brute_force(P,Q):
    min_dis = sys.float_info.max
    for i in range(0,len(P)):
        for j in range(i+1,len(Q)):
            distance = SED([P[i],Q[i]], [P[j],Q[j]])
            if distance < min_dis:
                min_dis = distance
    return min_dis

def effRec(P,Q):
    print('test recursive:O(nlogn)')
    start = time.time()
    min_dis = EfficientClosestPair(P,Q)
    starte = time.time()
    print('The closest distance by recursive:',min_dis)
    print('The time use for recursive',starte - start)

def effBF(P,Q):
    print('test brute force:O(n^2)')
    start1 = time.time()
    min_dis = brute_force(P,Q)
    start2 = time.time()
    print ('The closest distance by brute force:',min_dis)
    print ('The time use for brute force',start2 - start1)

def sortarray(P,Q):
    items = points
    new_items=(sorted(items,key=lambda x:(x[0],x[1])))
    points_list = numpy.array(new_items)
    P = points_list[:,0]
    Q = points_list[:,1]
    return [P,Q]

def EfficientClosestPair(P,Q):
    if len(P) <= 3:
        return brute_force(P,Q)
    else:
        Pl=[]
        Ql=[]
        Pr=[]
        Qr=[]

        mid = len(P)/2

        Pl = P[:math.ceil(mid/2)]
        Ql = Q[:math.ceil(mid/2)]
        Pr = P[math.floor(mid/2):]
        Qr = Q[math.floor(mid/2):]


        Dl = EfficientClosestPair(Pl,Ql)
        Dr = EfficientClosestPair(Pr,Qr)
        d = min(Dl,Dr)

        m = P[math.ceil(len(P)/2)-1]

        S=[]
        for index in range(0,len(Q)):
            if math.fabs(P[index]-m)<d:
                S.append([P[index],Q[index]])
    

        dminsq=d**2
        num=len(S)
        for i in range(0, num-2):
            k = i+1
            while (k<= num-1 ) and (((S[k][1]-S[i][1])**2) < dminsq):
                dminsq = min((S[k][0]-S[i][0])**2+(S[k][1]-S[i][1])**2,dminsq)
                k = k+1
        return math.sqrt(dminsq)


if __name__ == '__main__':
    effBF(P,Q)
    [P,Q] = sortarray(P,Q)
    effRec(P,Q)
