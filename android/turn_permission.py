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
    list_dirs = os.listdir(Path)
    list_dirs.sort(key=lambda x:int(x[:-4]))
    feature_list = []  # save all feature vectors
    for f in list_dirs:

        nowpath = os.path.join(Path,f)
        # savedpath = os.path.join(savepath,f)
        try:
            feature_sample = get_features(nowpath,features)
            # print (feature_sample,'\n',np.sum(feature_sample))
            feature_list.append(feature_sample)
        except:
            print(nowpath + 'is lost.')
            lostnum += 1
            lostname.append(f)

    # features_num = len(features)
    # print (features)
    # print (features_num)

    print ('lostnum is ' + str(lostnum))
    print ('lostname is ' + '\n',lostname)
    feature_list = np.array(feature_list)
    print (feature_list,feature_list.shape,2440*158,feature_list.sum())
    np.savetxt('/home/huu/Downloads/apks/' + 'Permission_Matrix.csv', feature_list)