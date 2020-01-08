from sklearn.ensemble import RandomForestClassifier as RF
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,precision_score,recall_score
from collections import Counter
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import csv
import time

def loaddata(features, labels):
    birth_data = []
    with open(features) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)
    train = np.array(birth_data, dtype=np.int8)

    birth_data = []
    with open(labels) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)
    test_ = np.array(birth_data, dtype=np.int8)
    test = list()
    for i in test_:
        for ii in i:
            test.append(ii)
    test = np.array(test)
    return train, test

def predict_RF(train,test):
    # 平均准确率归零
    avgscore = 0
    recallscore = 0
    precisionscore = 0
    N = 10

    # 进行十次测试
    for i in range(N):
        # 以10%的比例进行交叉验证
        X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.1)

        # 进行训练
        print('train...')
        # 进行SVC训练 使用线性核
        srf = RF(n_estimators=30, n_jobs=-1)
        srf.fit(X_train, y_train)

        # 预试
        print('test...')
        c_test = srf.predict(X_test)

        # print(y_test)
        # print(c_test)

        # 计算预测划分准确率
        print('accurary...')
        score = srf.score(X_test, y_test)
        print(classification_report(y_test, c_test))
        avgscore = avgscore + score
        recallscore = recallscore + recall_score(y_test, c_test, average="macro")
        precisionscore = precisionscore + precision_score(y_test, c_test, average="macro")
        print(score)

        # 通过混淆矩阵进行结果标示
        cm = confusion_matrix(y_test, c_test)
        np.set_printoptions(threshold=1000000)
        np.set_printoptions(precision=2)
        print('Confusion matrix, without normalization')
        print(str(cm))

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
    # return avgscore


if __name__ == "__main__":
    time1 = time.time()
    features = '/home/huu/Downloads/apkss/train.csv'
    # features = '/home/huu/Downloads/apkss/feature_selected_all.csv'
    labels = '/home/huu/Downloads/apkss/label.csv'
    savepath = "/home/huu/Downloads/apkss/select_train.csv"

    train,test = loaddata(features,labels)

    predict_RF(train, test)

    time2 = time.time()
    print('Time cost is ', (time2 - time1) / 60, 'min')