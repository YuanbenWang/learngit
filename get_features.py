import numpy as np
'''
total = ['a','b','c','d','e','f','g','h']
a = ['a','g','b','d']
b = ['b','d','f','h']
c = [a,b]
# fea = np.zeros((8))
fea_a = list()
for i in c:
    fea = np.zeros((8),dtype=int)
    for index,feature in enumerate(total):
          if feature in i :
                   fea[index] = 1
    fea_a.append(fea)
print(fea_a)
'''


def get_feature_vecor(dictionary,sample_list):
    fea_a = list()
    for each_sample in sample_list:
        feature_vecor = np.zeros((len(dictionary)),dtype=np.int8)
        for index,feature in enumerate(dictionary):
            if feature in each_sample :
                feature_vecor[index] = 1
        fea_a.append(feature_vecor)
    return np.array(fea_a)

if __name__ == '__main__':
    total = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    a = ['a', 'g', 'b', 'd']
    b = ['b', 'd', 'f', 'h']
    c = [a, b]
    list = get_feature_vecor(total,c)
    print (0)