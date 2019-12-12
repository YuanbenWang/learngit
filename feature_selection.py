import numpy as np
import pandas as pd


def Gini_calculation(test):
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

def calculate(index0,test):
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
    return G0

def Gini_A(train,test,num):  # num is the index of feature
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

    G0 = calculate(index0,test)
    G1 = calculate(index1,test)

    return (G0*px0+G1*px1)

def Gini_delta(Gini,train,test,num):
    add = Gini_A(train,test,num)
    return (Gini - add)

def Chi_square(i,j,train):
    a = b = c = d = 0
    n = len(train)
    for line in range(n):
        if train[line][i] == train[line][j]:
            if train[line][i] == 1:
                a += 1
            else:
                d += 1
        else:
            if train[line][i] == 1:
                c += 1
            else:
                b += 1
    if  (a+c+b+d) == (n):
        print ('Result is right.')

    return n*((a*d-b*c)**2)/(a+c)/(a+d)/(c+d)/(b+d)

def feature_select(train,test):
    flag = True
    Gini = Gini_calculation(test)
    while flag:
        flag_find = False
        for i in range(len(train[0])) :
            for j in range(len(train[0])):
                if i == j :
                    continue
                Chi = Chi_square(i,j,train)
                if Chi > 3.84:
                    flag_find = True
                    a = Gini_delta(Gini,train,test,i)
                    b = Gini_delta(Gini,train, test, j)
                    if a > b:
                        train = np.delete(train, j, axis=1)
                    else:
                        train = np.delete(train, i, axis=1)
                    break
            if flag_find:
                break
        if not flag_find:
            flag = False
    return train
