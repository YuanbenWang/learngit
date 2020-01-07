#coding=utf-8
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
import os


def get_permissions(filename,savepath,savepath2):

    app = apk.APK(filename)
    info = app.get_permissions()
    pathPart = filename.split("/")
    name = pathPart[-1].split('.')
    savepathss = os.path.join(savepath, name[0]) + '.txt'
    savepathss2 = os.path.join(savepath2, name[0]) + '.txt'
    fm = open(savepathss, 'w')
    fm2 = open(savepathss2, 'w')
    # fm.write(str)
    # fm.write("\n")
    list = []
    for i in info:
        tmp = i.split('.')
        final = tmp[-1]
        if final not in list:
            list.append(final)
            fm2.write(i)
            fm2.write("\n")
            fm.write(final)
            fm.write("\n")
    fm.close()
    fm2.close()

if __name__ == '__main__':
    # Path = '/home/huu/Downloads/apks/apk'
    # savepath = '/home/huu/Downloads/apks/apk_permissions'
    # savepath2 = '/home/huu/Downloads/apks/apk_permissions_initial'

    Path = '/home/huu/Downloads/apks/virr'
    savepath = '/home/huu/Downloads/apks/virtus_permissions'
    savepath2 = '/home/huu/Downloads/apks/virtus_permissions_initial'
    if not os.path.isdir(savepath):
        os.makedirs(savepath)
    if not os.path.isdir(savepath2):
        os.makedirs(savepath2)

    # Traverse all files and get the Image of the corresponding one
    error_list = []
    list_dirs = os.walk(Path)
    for root, dirs, files in list_dirs:

        for f in files:

            # pathPart = root.split("/")

            # print(newname)
            # # print os.path.join(root, fpart[0])
            # os.rename(os.path.join(root, f),os.path.join(root,newname))
            # # print 1
            paths = os.path.join(root,f)
            print (paths)
            try:
                get_permissions(paths, savepath, savepath2)
            except:
                error_list.append(paths)
                print (paths + ' is lost.')
            # try:
            #     get_permissions(newname,savepath)
            # except:
            #     print('lost.')

    print(len(error_list))