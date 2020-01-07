#coding=utf-8
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
import os


def get_apis(filename,savepath):
    app = apk.APK(filename)
    app_dex = dvm.DalvikVMFormat(app.get_dex())
    app_x = analysis.Analysis(app_dex)
    methods = set()
    cs = [cc.get_name() for cc in app_dex.get_classes()]

    for method in app_dex.get_methods():
        g = app_x.get_method(method)
        if method.get_code() == None:
            continue

        for i in g.get_basic_blocks().get():
            for ins in i.get_instructions():
                output = ins.get_output()
                match = re.search(r'(L[^;]*;)->[^\(]*\([^\)]*\).*', output)
                if match and match.group(1) not in cs:
                    methods.add(match.group())

    methods = list(methods)
    methods.sort()

    # save the apis to the savepathss
    pathPart = filename.split("/")
    name = pathPart[-1].split('.')
    savepathss = os.path.join(savepath, name[0]) + '.txt'
    fm = open(savepathss, 'w')
    for i in methods:
        fm.write(i)
        fm.write("\n")
    fm.close()

if __name__ == '__main__':
    Path = '/home/huu/Downloads/apkss/white'
    savepath = '/home/huu/Downloads/apkss/white_apis'

    if not os.path.isdir(savepath):
        os.makedirs(savepath)

    # Traverse all files and get the Image of the corresponding one
    error_list = []

    list_dirs = os.listdir(Path)


    feature_list = []  # save all feature vectors

    for f in list_dirs:
        if f.endswith('.apk'):
            # pathPart = root.split("/")

            # print(newname)
            # # print os.path.join(root, fpart[0])
            # os.rename(os.path.join(root, f),os.path.join(root,newname))
            # # print 1
            paths = os.path.join(Path,f)
            print (paths)
            try:
                get_apis(paths, savepath)
            except:
                error_list.append(paths)
                print (paths + ' is lost.')
            # try:
            #     get_permissions(newname,savepath)
            # except:
            #     print('lost.')

    print(len(error_list),'\n',)
    for i in error_list:
        print (i)