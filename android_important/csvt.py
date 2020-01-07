import numpy as np
import csv
import time

features = '/home/huu/Downloads/apkss/train.csv'
labels = '/home/huu/Downloads/apkss/label.csv'
savepath = "/home/huu/Downloads/apkss/select_train_test.csv"

a = np.array([[1,2,3],[4,5,6]])

with open(savepath, 'a', newline="") as ff:
    csv_w = csv.writer(ff)
    csv_w.writerows(a)