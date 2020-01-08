from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import datasets
from sklearn.naive_bayes import BernoulliNB
import numpy as np
from math import e
import csv
import time

def loaddata(features,labels):
    birth_data = []
    with open(features) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)
    train = np.array(birth_data,dtype=np.int8)

    birth_data = []
    with open(labels) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)
    test_ = np.array(birth_data, dtype=np.int8)
    test = list()
    for i in test_:
        for ii in i :
            test.append(ii)
    test = np.array(test)
    return train ,test

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
                b += 1
            else:
                c += 1
    if  a+c==0 or a+b==0 or c+d==0 or b+d==0:
        return 1

    return n*((a*d-b*c)**2)/(a+c)/(a+b)/(c+d)/(b+d)

if __name__=="__main__":
    features = '/home/huu/Downloads/apkss/train.csv'
    # features = '/home/huu/Downloads/apkss/feature_selected_all.csv'
    labels = '/home/huu/Downloads/apkss/label.csv'
    time1 = time.time()



    train, labelss = loaddata(features,labels)

    # set default
    accuracy = fpr = fnr = 0
    NN = 10

    for qq in range(NN):

        print(qq)
        X_train, X_test, y_train, y_test = train_test_split(train,labelss, test_size=0.1)

        # calcuate the Chi_square
        data = np.column_stack((X_train,y_train))
        # data = np.hstack((X_train,y_train))
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
            if s == 0:
                list0.append(X_train[i])
            else:
                list1.append(X_train[i])
        X_train_0 = np.array(list0)
        X_train_1 = np.array(list1)
        del list0
        del list1

        abbb=len(X_train_0)

        # P_x_equal_1_c0 = np.log(np.sum(X_train_0, axis=0)) -  np.log(len(X_train_0))
        # tmp = np.full(np.shape(X_train_0[0]),e)
        # tmp2 = np.power(tmp,P_x_equal_1_c0)
        # P_x_equal_0_c0 = np.log(tmp2 - np.ones(np.shape(tmp2)))
        #
        # P_x_equal_1_c1 = np.log(np.sum(X_train_1, axis=0)) - np.log(len(X_train_0))
        # tmp = np.full(np.shape(X_train_1[0]), e)
        # tmp2 = np.power(tmp, P_x_equal_1_c1)
        # P_x_equal_0_c1 = np.log(tmp2 - np.ones(np.shape(tmp2)))

        P_x_equal_1_c0 = np.sum(X_train_0, axis=0) / len(X_train_0)
        P_x_equal_0_c0 = 1 - P_x_equal_1_c0

        P_x_equal_1_c1 = np.sum(X_train_1, axis=0) / len(X_train_1)
        P_x_equal_0_c1 = 1 - P_x_equal_1_c1




        predict_right = 0
        predict_1 = 0
        predict_0 = 0
        TP = FN = FP = 0

        predict_sum = len(y_test)

        # for raw_num,line in enumerate(X_test):
        #
        #     # calculate the P_(c1|X),P_(c0|X)
        #     P_c1x = np.log(P_c1)
        #     P_c0x = np.log(P_c0)
        #     for index,j in enumerate(line):
        #         if j == 1:
        #             P_c1x += P_x_equal_1_c1[index]
        #             P_c1x += np.log(Chi_list[index])
        #
        #
        #             P_c0x += P_x_equal_1_c0[index]
        #             P_c0x += np.log(Chi_list[index])
        #         else:
        #             P_c1x += P_x_equal_0_c1[index]
        #             P_c0x += P_x_equal_0_c0[index]
        #
        #     if P_c1x > P_c0x:
        #         predict_label = 1
        #         predict_1 += 1
        #     else:
        #         predict_label = 0
        #         predict_0 += 1
        #
        #     if predict_label == y_test[raw_num][0]:
        #         predict_right += 1
        #         if predict_label == 1:
        #             TP += 1
        #     else:
        #         if predict_label == 1:
        #             FP += 1
        #         else:
        #             FN += 1
        for raw_num,line in enumerate(X_test):

            # calculate the P_(c1|X),P_(c0|X)
            P_c1x = P_c1
            P_c0x = P_c0
            for index,j in enumerate(line):
                if j == 1:
                    P_c1x *= P_x_equal_1_c1[index]
                    P_c1x *= Chi_list[index]


                    P_c0x *= P_x_equal_1_c0[index]
                    P_c0x *= Chi_list[index]
                else:
                    P_c1x *= P_x_equal_0_c1[index]
                    P_c0x *= P_x_equal_0_c0[index]

            if P_c1x > P_c0x:
                predict_label = 1
                predict_1 += 1
            else:
                predict_label = 0
                predict_0 += 1

            if predict_label == y_test[raw_num]:
                predict_right += 1
                if predict_label == 1:
                    TP += 1
            else:
                if predict_label == 1:
                    FP += 1
                else:
                    FN += 1
        accuracy += predict_right / predict_sum
        fpr += FP / (FP + TP)
        fnr += FN / (FN + TP)



    # accuracy = predict_right / predict_sum
    # fpr = FP / (FP + TP)
    # fnr = FN / (FN + TP)
    accuracy /= NN
    fpr /= NN
    fnr /= NN
    print('accuracy:',accuracy)
    print('FPR:',fpr)
    print('FNR:', fnr)

    time2 = time.time()
    print('Time cost is ', (time2 - time1) / 60, 'min')
    
