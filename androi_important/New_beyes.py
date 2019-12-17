from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import datasets
from sklearn.naive_bayes import BernoulliNB
import numpy as np
from math import e
import csv

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
    if  a+c==0 or a+d==0 or c+d==0 or b+d==0:
        return 1

    return n*((a*d-b*c)**2)/(a+c)/(a+d)/(c+d)/(b+d)

if __name__=="__main__":
    features = '/home/huu/Downloads/apkss/train.csv'
    labels = '/home/huu/Downloads/apkss/label.csv'

    t = []
    with open(features, 'r', newline="") as fff:
        csv_w = csv.reader(fff)
        for line in csv_w:
            t.append(line)
    train = np.array(t,dtype=np.int8)

    t = []
    with open(features, 'r', newline="") as fff:
        csv_w = csv.reader(fff)
        for line in csv_w:
            t.append(line)
    labelss = np.array(t, dtype=np.int8)
    del t





    X_train, X_test, y_train, y_test = train_test_split(train,labelss, test_size=0.1)

    # calcuate the Chi_square
    data = np.hstack((X_train,y_train))
    Chi_list = []
    for i in range(len(data[0])-1):
        Chi_list.append(Chi_square(i, -1, data))
    del data


    # prior probability
    P_c1 = y_train.sum() / len(y_train)
    P_c0 = 1 - P_c1

    # divide the train to 0 and 1
    list0 = []
    list1 = []
    for i,s in enumerate(y_train):
        if s[0] == 0:
            list0.append(X_train[i])
        else:
            list1.append(X_train[i])
    X_train_0 = np.array(list0)
    X_train_1 = np.array(list1)
    del list0
    del list1

    abbb=len(X_train_0)
    print(1)
    P_x_equal_1_c0 = np.log(np.sum(X_train_0, axis=0)) -  np.log(len(X_train_0))
    tmp = np.full(np.shape(X_train_0[0]),e)
    tmp2 = np.power(tmp,P_x_equal_1_c0)
    P_x_equal_0_c0 = np.log(tmp2 - np.ones(np.shape(tmp2)))

    P_x_equal_1_c1 = np.log(np.sum(X_train_1, axis=0)) - np.log(len(X_train_0))
    tmp = np.full(np.shape(X_train_1[0]), e)
    tmp2 = np.power(tmp, P_x_equal_1_c1)
    P_x_equal_0_c1 = np.log(tmp2 - np.ones(np.shape(tmp2)))

    del tmp
    del tmp2



    predict_right = 0
    predict_1 = 0
    predict_0 = 0
    TP = FN = FP = 0
    predict_sum = len(y_test)

    for raw_num,line in enumerate(X_test):

        # calculate the P_(c1|X),P_(c0|X)
        P_c1x = np.log(P_c1)
        P_c0x = np.log(P_c0)
        for index,j in enumerate(line):
            if j == 1:
                P_c1x += P_x_equal_1_c1[index]
                P_c1x += np.log(Chi_list[index])


                P_c0x += P_x_equal_1_c0[index]
                P_c0x += np.log(Chi_list[index])
            else:
                P_c1x += P_x_equal_0_c1[index]
                P_c0x += P_x_equal_0_c0[index]

        if P_c1x > P_c0x:
            predict_label = 1
            predict_1 += 1
        else:
            predict_label = 0
            predict_0 += 1

        if predict_label == y_test[raw_num][0]:
            predict_right += 1
            if predict_label == 1:
                TP += 1
        else:
            if predict_label == 1:
                FP += 1
            else:
                FN += 1




    accuracy = predict_right / predict_sum
    print('accuracy:',accuracy)
    fpr = FP / (FP + TP)
    print('FPR:',fpr)
    fnr = FN / (FN + TP)
    print('FNR:', fnr)