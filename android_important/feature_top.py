import numpy as np
import csv
import time
import os

def load_data(features,labels):
    birth_data = []
    with open(features) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data.append(row)
    train = np.array(birth_data, dtype=np.int8)

    birth_data2 = []
    with open(labels) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
            birth_data2.append(row)
    test_ = np.array(birth_data2, dtype=np.int8)
    test = list()
    for i in test_:
        for ii in i:
            test.append(ii)

    test = np.array(test)
    return train,test

def get_selected_fateures(train,train_argsort,num,dictionary):
    train_new = []
    dict_new = []
    train_argtop1000 = train_argsort[:num] # 927 top1000
    for i in train_argtop1000:
        train_new.append(train[:, i])
        dict_new.append(dictionary[i])
    train_new = np.array(train_new).T
    return train_new,dict_new

if __name__ == "__main__":
    time1 = time.time()
    features = '/home/huu/Downloads/apkss/train.csv'
    labels = '/home/huu/Downloads/apkss/label.csv'
    features_dict = '/home/huu/Downloads/apkss/features.txt'
    # savepath = "/home/huu/Downloads/apkss/select_train.csv"
    savepath = '/home/huu/Downloads/apkss/feature_selected'


    # get the numbers of features, and the sorted numbers of features
    train, label = load_data(features, labels)
    train_sum = train.sum(axis=0)
    train_argsort = np.argsort(-train_sum)
    train_sort = np.sort(train_sum)[::-1]

    # get all the features' name
    f_all = open(features_dict, 'r')
    inf = f_all.readlines()
    dictionary = [i.strip('\n') for i in inf]
    f_all.close()

    # get feature top
    feature_top = [200,300,500,800,1000]

    for index,element in enumerate(feature_top):
        train_new,dict_new = get_selected_fateures(train, train_argsort, element,dictionary)

        # save data and dictionary
        file_name = "%d.csv" % (element)
        dict_name = "%d.txt" % (element)
        savepath2 = os.path.join(savepath,file_name)
        savepath3 = os.path.join(savepath,dict_name)
        with open(savepath2, 'a', newline="") as ff:
            csv_w = csv.writer(ff)
            csv_w.writerows(train_new)
        with open(savepath3, 'w') as fm:
            for i in dict_new:
                fm.write(i)
                fm.write("\n")



    print("over.")
    time2 = time.time()

    print('Time cost is ', (time2 - time1) / 60, 'min')

