import numpy as np
import os
import time
import csv

def get_feature_vecor(dictionary,sample_list):

    feature_vecor = np.zeros((len(dictionary)), dtype=np.int8)
    sum = 0
    for index,feature in enumerate(dictionary):
        if feature in sample_list :
            feature_vecor[index] = 1
            sum += 1
    return feature_vecor,sum

if __name__ == '__main__':
    time1 = time.time()

    whitePath_sample = '/home/huu/Downloads/apks/all_features_white'
    blackPath_sample = '/home/huu/Downloads/apks/all_features_black'
    # Path_sample = '/home/huu/Downloads/apks/a_fea'
    Path_dic = '/home/huu/Downloads/apks/features.txt'
    train = '/home/huu/Downloads/apks/train.csv'
    label = '/home/huu/Downloads/apks/label.csv'

    # get all the features' name
    f_all = open(Path_dic,'r')
    inf = f_all.readlines()
    dictionary = [i.strip('\n') for i in inf]
    f_all.close()

    error_list = []
    # train_all = []  # save all feature vectors
    # test_all = []

    list_dirs = os.listdir(whitePath_sample)
    for f in list_dirs:

        paths = os.path.join(whitePath_sample, f)
        print(paths)
        try:
            fo = open(paths,'r')
            sample_ = fo.readlines()
            fo.close()
            sample_list = [i.strip('\n') for i in sample_]
            vector,sum  = get_feature_vecor(dictionary,sample_list)
            print (sum)

            with open(train,'a',newline="") as ff:
                csv_w = csv.writer(ff)
                csv_w.writerow(vector)

            with open(label, 'a', newline="") as fff:
                csv_w = csv.writer(fff)
                csv_w.writerow([1])

        except:
            error_list.append(paths)
            print(paths + ' is lost.')



    list_dirs = os.listdir(blackPath_sample)
    for f in list_dirs:

        paths = os.path.join(blackPath_sample, f)
        print(paths)
        try:
            fo = open(paths, 'r')
            sample_ = fo.readlines()
            fo.close()
            sample_list = [i.strip('\n') for i in sample_]
            vector, sum = get_feature_vecor(dictionary, sample_list)
            print(sum)

            with open(train, 'a', newline="") as ff:
                csv_w = csv.writer(ff)
                csv_w.writerow(vector)

            with open(label, 'a', newline="") as fff:
                csv_w = csv.writer(fff)
                csv_w.writerow([0])

        except:
            error_list.append(paths)
            print(paths + ' is lost.')
    # train_all = np.array(train_all)
    # test_all = np.array(test_all)
    # print (train_all,'\n',train_all.shape)
    # print (test_all.shape)
    #
    print(len(error_list))
    print(error_list)
    # np.savetxt(train, train_all, delimiter=',')
    # np.savetxt(test, test_all, delimiter=',')

    time2 = time.time()

    print('Time cost is ',(time2-time1)/60,'min')