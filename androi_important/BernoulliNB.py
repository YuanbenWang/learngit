from sklearn import datasets
from sklearn.naive_bayes import BernoulliNB
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.linear_model import LinearRegression
from scipy import stats
import pylab as pl
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, recall_score, precision_score
import math


features = '/home/huu/Downloads/apkss/train.csv'
labels = '/home/huu/Downloads/apkss/label.csv'
savepath = "/home/huu/Downloads/apkss/select_train.csv"

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
del test_

# load data
# iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(train, test, test_size=0.1)
clf = BernoulliNB()
clf = clf.fit(X_train, y_train)



print('test...')
c_test = clf.predict(X_test)



# 计算预测划分准确率
print('accurary...')
score = clf.score(X_test, y_test)

print(classification_report(y_test, c_test))
print(score)

# 通过混淆矩阵进行结果标示
cm = confusion_matrix(y_test, c_test)
np.set_printoptions(threshold=10000000)
np.set_printoptions(precision=2)
print('Confusion matrix, without normalization')
print(str(cm))


