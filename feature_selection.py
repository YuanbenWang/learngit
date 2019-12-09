import numpy as np
import pandas as pd


def Gini_calculation(train,test):
    count1 = 0
    count0 = 0
    for line in test:
        if line == 0:
            count0 += 1
        else:
            count1 += 1
    p0 = count0 / (count0 + count1)
    p1 = count1 / (count0 + count1)
    return (1-p0**2-p1**2)

def Gini_A(train,test,num):  # num is the order of feature
    index0 = []
    index1 = []

    for index,line in enumerate(train):
        if line[num] == 0:
            index0.append(index0)
        else:
            index1.append(index1)

    length = len(train)
    px1 = len(index1) / length
    px0 = len(index0) / length

    # calculate the G(Y|X=0),G = 1-p0**2-p1**2
    count0 = 0
    count1 = 0
    for i in index0:
        if test[i] == 0:
            count0 += 1
        else:
            count1 += 1
    p0 = count0 / (count0 + count1)
    p1 = count1 / (count0 + count1)
    G0 = (1 - p0 ** 2 - p1 ** 2)

    count0 = 0
    count1 = 0
    for i in index1:
        if test[i] == 0:
            count0 += 1
        else:
            count1 += 1
    p0 = count0 / (count0 + count1)
    p1 = count1 / (count0 + count1)
    G1 = (1 - p0 ** 2 - p1 ** 2)

    return (G0*px0+G1*px1)

def Gini_delta(train,test,num):
    Gini = Gini_calculation(train,test)
    add = Gini_A(train,test,num)
    return (Gini - add)