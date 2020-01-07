import re
import os
import numpy as np


def get_features(nowpath, savedpath):
    print(nowpath)
    # global count
    fo = open(nowpath, 'r')
    info = fo.readlines()
    for i in info:
        i = i.strip()
        if i not in features:
            features.append(i)
    fo.close()


# def turn_features(nowpath,savedpath,features_num):
#     fo = open(nowpath, 'r')
#     info = fo.readlines()
#     for i in info:
#         i = i.strip()
#         if i not in features:
#             features.append(i)
#     fo.close()


if __name__ == '__main__':
    Path = '/home/huu/Downloads/apks/apk_permissions'
    savepath = '/home/huu/Downloads/apks/apk_permissions_features'

    if not os.path.isdir(savepath):
        os.makedirs(savepath)

    # Traverse all files and get the Image of the corresponding one
    lostnum = 0
    features = []
    file = open('permission_google.txt', 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        features.append(line)
    feanum = len(features)

    list_dirs = os.walk(Path)
    for root, dirs, files in list_dirs:

        for f in files:
            nowpath = os.path.join(root, f)
            savedpath = os.path.join(savepath, f)
            try:
                get_features(nowpath, savedpath)
            except:
                print(nowpath + 'is lost.')
                lostnum += 1

    # features_num = len(features)
    # print (features)
    # print (features_num)

    print('lostnum is ' + str(lostnum))






import re
import os
import numpy as np



def get_features(nowpath,features):
    print (nowpath)
    fo = open(nowpath,'r')
    inf = fo.readlines()
    info = [i.strip() for i in inf ]
    feanum = len(features)
    feature_sample = np.zeros(feanum,np.int)
    for index,feature in enumerate(features):
        if feature in info :
            feature_sample[index] = 1
    # feature_list.append(feature_sample)
    fo.close()
    return feature_sample



if __name__ == '__main__':
    Path = '/home/huu/Downloads/apks/apk_permissions'
    savepath = '/home/huu/Downloads/apks/apk_permissions_features'

    if not os.path.isdir(savepath):
        os.makedirs(savepath)

    lostnum = 0
    lostname = []

    # Get all permission from txt
    file = open('permission_google.txt','r')
    features = file.readlines()
    features = [i.strip() for i in features]


    # Traverse all files and get the Image of the corresponding one
    list_dirs = os.walk(Path)
    feature_list = []  # save all feature vectors
    for root, dirs, files in list_dirs:

        for f in files:
            nowpath = os.path.join(root,f)
            savedpath = os.path.join(savepath,f)
            try:
                feature_sample = get_features(nowpath,features)
                # print (feature_sample,'\n',np.sum(feature_sample))
            except:
                print(nowpath + 'is lost.')
                lostnum += 1
                lostname.append(f)

    # features_num = len(features)
    # print (features)
    # print (features_num)

    print ('lostnum is ' + str(lostnum))
    print ('lostname is ' + '\n',lostname)