from itertools import combinations
import sys
import time
import numpy as np


def brute_force(Capacity,weight,value):
    n = len(weight)
    A = [0 for x in range(pow(2,n))]
    bestValue = 0
    bestWeight = 0
    for i in range(1,pow(2,n)):
        j = n
        tempWeight = 0
        tempValue = 0
        while(A[j] != 0 and j > 0):
            A[j] = 0
            j = j - 1
        A[j] = 1
        for k in range(1,n):
            if(A[k]==1):
                tempWeight = tempWeight + weight[k]
                tempValue = tempValue + value[k]
        if((tempValue > bestValue) and (tempWeight<=Capacity)):
            bestValue = tempValue
            bestWeight = tempWeight
        bestChoice = A
    return bestValue

def dynamic_programming(Capacity, weight, value):
    n = len(weight)
    K = [[0 for x in range(Capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(Capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][Capacity]


def greedyalgorithm(Capacity, weight,value):
    CumWeight = 0
    r  = [10 for x in range(len(weight))]
    for i in range(len(weight)):
        r[i] = value[i] / weight[i]

    order = sorted(range(len(r)), key=lambda k: r[k],reverse = True)
    weight[:] = [weight[i] for i in order]  # [:] is key!
    value[:] = [value[i] for i in order]  # [:] is key!

    A = [0 for x in range(len(weight))]
    w = 0
    for i in range(0,len(weight)):
        if w + weight[i] <= Capacity:
            A[i] = 1
            w = w + weight[i]
        else:
            A[i] = (Capacity - w) / weight[i]
            w = Capacity
            break
    a = np.array(A)
    b = np.array(value).transpose()
    c = np.array(weight).transpose()
    #print(A)
    #print(value)
    #print(sum(a*c))
    return sum(a*b)




def testAll(Capacity,weight,value):#function to test all 3 functions


    print('\nTesting Brute Force\n')
    t0=time.time()
    resultBF=brute_force(Capacity,weight,value)
    t1=time.time()
    T=t1-t0
    print('optimal value: ' + str(resultBF))
    print('Time use: ' + str(T) + ' seconds.\n')


    print('\nTesting Dynamic Programming\n')
    t0=time.time()
    resultDP=dynamic_programming(Capacity,weight,value)
    t1=time.time()
    T=t1-t0
    print('optimal value: ' + str(resultDP))
    print('Time use: ' + str(T) + ' seconds.\n')



    print('\nTesting Greedy Algorithm\n')
    t0=time.time()
    resultga=greedyalgorithm(Capacity,weight,value)
    t1=time.time()
    T=t1-t0
    print('optimal value: ' + str(resultga))
    print('Time use: ' + str(T) + ' seconds.\n')

    return


if __name__ == '__main__':
    print('Solution	for	Knapsack Problem')
    if len(sys.argv)>2:
        raise ValueError
    if len(sys.argv)>1:
        filename=str(sys.argv[1])
    else:
        filename="input3.txt"
    try:
        f = open(filename, "r")
        array = f.read()
        weight=[]
        value=[]
        Array=[]
        Capacity=0

        Array=array.splitlines(0)
        Capacity=Array[0]
        weight=Array[1]
        value=Array[2]

        weight = weight.split(',')
        value = value.split(',')

        Ivalue = [int(v) for v in value]
        Iweight = [int(w) for w in weight]

        if len(weight) != len(value):
            raise ValueError

    except IOError:
        print ("Can't read file:"+str(filename))
        sys.exit()
    except ValueError:
        print ("the input value is invalid")
        sys.exit()
    else:
        Capacity = int(Capacity)
        print ('\n input file: ' +filename+' is: ')
        print ('   The Capacity: ' +str(Capacity))
        print ('   Weights of each item: ' +str(weight))
        print ('   Valuesc of each item:  ' +str(value))
        print ('   Number of items: '+str(len(weight)))
        testAll(Capacity,Iweight,Ivalue)