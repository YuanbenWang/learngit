import numpy as np
import cv2
from PIL import Image
from sklearn.feature_extraction.text import TfidfTransformer
#from pylab import *
#import matplotlib.pyplot as plt
import time
import os
import csv
# from matplotlib.font_manager import FontProperties

# 图像的LBP原始特征计算算法：将图像指定位置的像素与周围8个像素比较
# 比中心像素大的点赋值为2，相等为1，比中心像素小的赋值为0
def calute_basic_lbp(image_array, i, j):
    sum = []
    if image_array[i - 1, j - 1] > image_array[i, j]:
        sum.append(2)
    elif image_array[i - 1, j - 1] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i - 1, j] > image_array[i, j]:
        sum.append(2)
    elif image_array[i - 1, j] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i - 1, j + 1] > image_array[i, j]:
        sum.append(2)
    elif image_array[i - 1, j + 1] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i, j - 1] > image_array[i, j]:
        sum.append(2)
    elif image_array[i, j - 1] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i, j + 1] > image_array[i, j]:
        sum.append(2)
    elif image_array[i, j + 1] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i + 1, j - 1] > image_array[i, j]:
        sum.append(2)
    elif image_array[i + 1, j - 1] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i + 1, j] > image_array[i, j]:
        sum.append(2)
    elif image_array[i + 1, j] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    if image_array[i + 1, j + 1] > image_array[i, j]:
        sum.append(2)
    elif image_array[i + 1, j + 1] == image_array[i, j]:
        sum.append(1)
    else:
        sum.append(0)

    return sum


def lbp_basic(path):
    image = cv2.imread(path)
    image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    features = np.zeros(6561, np.int)  # 位置是三进制值，array值代表个数
    # basic_array = np.zeros(image_array.shape, np.int)
    width = image_array.shape[0]
    height = image_array.shape[1]
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            sum = calute_basic_lbp(image_array, i, j)
            result = 0    # result为8位三进制数
            for index,element in enumerate(sum):
                result += element * pow(3,index)
            # basic_array[i, j] = result
            features[result] += 1
    return features

def lbp_hist(path):
    image = cv2.imread(path)
    image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    features = np.zeros(6561, np.int)  # 位置是三进制值，array值代表个数
    # basic_array = np.zeros(image_array.shape, np.int)
    width = image_array.shape[0]
    height = image_array.shape[1]
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            sum = calute_basic_lbp(image_array, i, j)
            result = 0    # result为8位三进制数
            for index,element in enumerate(sum):
                result += element * pow(3,index)
            # basic_array[i, j] = result
            features[result] += 1
    return features / features.sum()

# 绘制图像原始LBP特征的归一化统计直方图
# 绘制指定维数和范围的图像灰度归一化统计直方图
# def show_hist(features):
#     # plt.bar(xx, features)
#     plt.hist(features,bins=10, histtype='bar', rwidth=0.8)
#     plt.legend()
#     plt.show()


if __name__ == '__main__':
    time1 = time.time()
    image_path = r'E:\virtus_test\10virtusImage'
    save_path = r'E:\virtus_test\lbp\LBP_HIST\10virtusImage'
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    list_dirs = os.walk(image_path)
    list_of_family_features = []
    label_list = []
    label_name = []
    number = 0
    count = 0
    label_str = ''
    for root, dirs, files in list_dirs:
        # for d in dirs:
        #     if not os.path.isdir(os.path.join(save_path, d)):
        #         os.makedirs(os.path.join(save_path, d))


        for f in files:

            pathPart = root.split("\\")
            ImageFamilyPath = os.path.join(image_path, pathPart[len(pathPart) - 1])
            ImageFilePath = os.path.join(ImageFamilyPath, f)
            print(os.path.join(root, f))
            try:
                features = lbp_hist(os.path.join(root, f))
                # print(features.sum())
                list_of_family_features.append(features)
                if pathPart[-1] != label_str:
                    label_str = pathPart[-1]
                    count += 1
                    label_name.append(label_str)
                label_list.append(count)
            except:
                number += 1
                print(1)




    # transformer = TfidfTransformer(smooth_idf=True)
    # tfidf = transformer.fit_transform(list_of_family_features)
    # family_features = tfidf.toarray()
    family_features = np.array(list_of_family_features)
    save_path_of_famlily = os.path.join(save_path,'all_features')
    with open(save_path_of_famlily + '.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(family_features)
    # print(family_features)
    save_path_of_famlily_label = os.path.join(save_path, 'label')+ '.txt'
    with open(save_path_of_famlily_label ,'w',newline='') as f:
        for fp in label_list:
            f.write(str(fp))
            f.write('\n')
    save_path_of_famlily_label = os.path.join(save_path, 'label_name') + '.txt'
    with open(save_path_of_famlily_label,'w',newline='') as f:
        for fp in label_name:
            f.write(fp)
            f.write('\n')

    print('Finish! number of the lost samples is ' + str(number))


    time2 = time.time()
    print('The cost time is ', (time2 - time1) / 60, ' min.')



