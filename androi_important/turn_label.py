import csv
import numpy as np
label = '/home/huu/Downloads/apkss/label.csv'
label2 = '/home/huu/Downloads/apkss/label2.csv'

t = []
with open(label, 'r', newline="") as fff:
    csv_w = csv.reader(fff)
    for line in csv_w:
        if line[0] == '1':
            t.append([0])
        else:
            t.append([1])
t=np.array(t)

with open(label2, 'a', newline="") as fff:
    csv_w = csv.writer(fff)
    csv_w.writerows(t)