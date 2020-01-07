from sklearn import datasets
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, recall_score, precision_score
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.linear_model import LinearRegression
from scipy import stats
import pylab as pl
from sklearn.neighbors import KNeighborsClassifier
import math




def load_data(features,labels):
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

def predict_NB(train, test):
    X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.1)
    BN = BernoulliNB()
    BN = BN.fit(X_train, y_train)

    # 平均准确率归零
    avgscore = 0
    recallscore = 0
    precisionscore = 0
    N = 10

    # 进行十次测试
    for i in range(N):
        print('test...')
        c_test = BN.predict(X_test)

        # 计算预测划分准确率
        print('accurary...')
        score = BN.score(X_test, y_test)
        print(classification_report(y_test, c_test))
        print(score)

        # 通过混淆矩阵进行结果标示
        cm = confusion_matrix(y_test, c_test)
        np.set_printoptions(threshold=10000000)
        np.set_printoptions(precision=2)
        print('Confusion matrix, without normalization')
        print(str(cm))
        avgscore = avgscore + score
        recallscore = recallscore + recall_score(y_test, c_test, average="macro")
        precisionscore = precisionscore + precision_score(y_test, c_test, average="macro")

    # 输出N次的平均准确率
    avgscore = avgscore / N
    recallscore = recallscore / N
    precisionscore = precisionscore / N

    print('avgscore....')
    print(avgscore)
    print('False positive rate')
    print(1 - precisionscore)
    print('false negative rate')
    print(1 - recallscore)
    return avgscore

def get_selected_fateures(train,train_argsort,num):
    train_new = []
    train_argtop1000 = train_argsort[:num] # 927 top1000
    for i in train_argtop1000:
        train_new.append(train[:, i])
    train_new = np.array(train_new).T
    return train_new

if __name__ == "__main__":
    features = '/home/huu/Downloads/apkss/train.csv'
    features = '/home/huu/Downloads/apkss/feature_selected/feature_auto_selected/800.csv'
    labels = '/home/huu/Downloads/apkss/label.csv'
    savepath = "/home/huu/Downloads/apkss/select_train.csv"
    train, label = load_data(features, labels)

    # # get the numbers of features, and the sorted numbers of features
    # train, label = load_data(features, labels)  # test is the label
    # train_sum = train.sum(axis=0)
    # train_argsort = np.argsort(-train_sum)
    # train_sort = np.sort(train_sum)[::-1]
    #
    # feature_M = [1750,1934,823,526,654]
    # result = []
    # for M in feature_M:
    #     train_new = get_selected_fateures(train, train_argsort, M)
    #     result.append(predict_NB(train, label))
    # print(result)


    # predict
    predict_NB(train, label)



