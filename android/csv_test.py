import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt


def loadcsv(features,labels):
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
    label_ = np.array(birth_data, dtype=np.int8)
    label = list()
    for i in label_:
        for ii in i :
            label.append(ii)

    label = np.array(label)
    del label_,birth_data
    return train,label

if __name__ == '__main__':
    features = r'train.csv'
    labels = r'label.csv'
    savepath = "/home/huu/Downloads/apkss/select_train.csv"
    train,label = loadcsv(features,labels)
    trainSum = train.sum(axis=0)

    # count = 0
    # countlist = []
    # threshold = 10
    # thresholdlist = []
    # while threshold <= 10000:
    #     count = 0
    #
    #     for index,element in enumerate(trainSum):
    #         if element < threshold:
    #             count += 1
    #     print(count)
    #     if count == 13282:
    #         print('Over,the threshold is %d' % threshold)
    #         break
    #     thresholdlist.append(threshold)
    #     countlist.append(count)
    #     threshold +=5
    #
    # plt.plot(thresholdlist,countlist)
    # plt.plot(thresholdlist,countlist, '.y')

    count = 0
    threshold = 1000
    fe_list= []
    for index, element in enumerate(trainSum):
        if element < threshold:
            count += 1
            fe_list.append(index)
    print(count)
    # plt.scatter(threshold, count)
    # plt.show()

    train2 = np.delete(train,fe_list,axis=1)


    with open('train2.csv', 'a', newline="") as ff:
        csv_w = csv.writer(ff)
        for ii in train2:
            csv_w.writerow(ii)

