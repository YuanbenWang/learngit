import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.linear_model import LinearRegression
from scipy import stats
import pylab as pl
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, recall_score, precision_score
import math
from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
#subfeatures=pd.read_csv('/home/houmo/Downloads/Yashu_cardiff/Data_New20180603/lbpBlock10Viruts/lbp_kmeans_hist_feature.csv',header=None)
#labels = pd.read_csv('/home/houmo/Downloads/Yashu_cardiff/Data_New20180603/lbpBlock10Viruts/ClassNo_full.csv',header=None)



# 平均准确率归零
avgscore = 0
recallscore = 0
precisionscore = 0
N = 10

# 进行十次KNN测试
for i in range(N):
    # 以10%的比例进行交叉验证
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)

    # 进行训练
    print('train...')
    # 进行SVC训练 使用线性核
    clf = SVC(kernel='linear')                     # 高斯核 rbf
    # clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # 预试
    print('test...')
    c_test = clf.predict(X_test)

    # print(y_test)
    # print(c_test)

    # 计算预测划分准确率
    print('accurary...')
    score = clf.score(X_test, y_test)
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
