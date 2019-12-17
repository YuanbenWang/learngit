import csv
import numpy as np
label = '/home/huu/Downloads/apkss/train.csv'
label2 = '/home/huu/Downloads/apkss/train2.csv'

t = []
count = 0
with open(label, 'r', newline="") as fff:
    csv_w = csv.reader(fff)
    for line in csv_w:
        t.append(line)
        if count >=4:
            break
        else:
            count += 1

t=np.array(t,dtype=np.int8)

with open(label2, 'a', newline="") as fff:
    csv_w = csv.writer(fff)
    csv_w.writerows(t)