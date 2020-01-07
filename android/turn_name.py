import os

if __name__ == '__main__':

    malwarePath = '/home/huu/Downloads/apks/virtus_sample'

    count = 3000
    # Traverse all files and get the Image of the corresponding one
    list_dirs = os.walk(malwarePath)
    for root, dirs, files in list_dirs:

        for f in files:
            strr = count
            newname = str(strr) + '.apk'
            # print os.path.join(root, fpart[0])
            os.rename(os.path.join(root, f),os.path.join(root,newname))
            count += 1
            # print 1
