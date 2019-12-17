import numpy as np
import csv
import time
"""
input: feature.csv,label.csv
output:feature_selcted.csv
"""

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
            index0.append(index)
        else:
            index1.append(index)

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
    # if  (a+c+b+d) == (n):
    #     print ('Result is right.')

    return n*((a*d-b*c)**2)/(a+c)/(a+d)/(c+d)/(b+d)

def feature_select(train,test):
    Gini = Gini_calculation(test)
    index_del = []

    for i in range(len(train[0])) :
        if i in index_del:
            continue
        for j in range(len(train[0])):
            if j in index_del:
                continue
            print(i,j)
            if i == j :
                continue
            Chi = Chi_square(i,j,train)
            print (Chi)
            if Chi > 3.84:
                a = Gini_delta(Gini,train,test,i)
                b = Gini_delta(Gini,train, test, j)
                if a > b:
                    if j in index_del:
                        pass
                    else:
                        index_del.append(j)
                else:
                    if i in index_del:
                        pass
                    else:
                        index_del.append(j)
    print(len(index_del))
    train = np.delete(train, index_del, axis=1)

    return train


if __name__ == "__main__":
    time1 = time.time()
    features = '/home/huu/Downloads/apkss/train.csv'
    labels = '/home/huu/Downloads/apkss/label.csv'
    savepath = "/home/huu/Downloads/apkss/select_train.csv"

    birth_data = []
    with open(features) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)
    train = np.array(birth_data,dtype=np.int8)

    birth_data2 = []
    with open(labels) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data2.append(row)
    test_ = np.array(birth_data2, dtype=np.int8)
    test = list()
    for i in test_:
        for ii in i :
            test.append(ii)

    test = np.array(test)
    del test_
    del birth_data
    del birth_data2


    new_features = feature_select(train,test)
    print(len(new_features[0]))

    with open(savepath, 'a', newline="") as ff:
        csv_w = csv.writer(ff)
        csv_w.writerow(new_features)

    print("over.")

    time2 = time.time()

    print('Time cost is ', (time2 - time1) / 60, 'min')

