#coding=utf-8
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
import os
from time import time

def get_apis(app):

    # get apis and keep it in methods
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
                    line = match.group()
                    index1 = line.find('>')
                    index2 = line.find('(')
                    line_ = line[index1+1:index2]
                    if len(line_) != 1:
                        methods.add(line_)

    methods = list(methods)


    return methods

def get_info(filename,savepath):

    # get permisson and api
    app = apk.APK(filename)
    permissions = app.get_permissions()
    methods = get_apis(app)

    # save them in power
    power = permissions + methods
    power.sort()

    # save all we get in txt
    pathPart = filename.split("/")
    name = pathPart[-1].split('.')
    savepathss = os.path.join(savepath, name[0]) + '.txt'
    fm = open(savepathss, 'w')
    for i in power:
        if i not in feature_list:
            feature_list.append(i)
        fm.write(i)
        fm.write("\n")
    fm.close()

if __name__ == '__main__':
    time1 = time()

    whitePath = '/home/huu/Downloads/apks/white'
    blackPath = '/home/huu/Downloads/apks/black'
    # Path = '/home/huu/Downloads/apks/apkt'
    savepath_white = '/home/huu/Downloads/apks/all_features_white'
    savepath_black = '/home/huu/Downloads/apks/all_features_black'
    featuresave = '/home/huu/Downloads/apks'

    if not os.path.isdir(savepath_white):
        os.makedirs(savepath_white)
    if not os.path.isdir(savepath_black):
        os.makedirs(savepath_black)

    error_list = []
    feature_list = []  # save all feature vectors


    list_dirs = os.listdir(whitePath)
    for f in list_dirs:

        paths = os.path.join(whitePath,f)
        print (paths)
        try:
            get_info(paths, savepath_white)
        except:
            error_list.append(paths)
            print (paths + ' is lost.')


    list_dirs = os.listdir(blackPath)
    for f in list_dirs:

        paths = os.path.join(blackPath, f)
        print(paths)
        try:
            get_info(paths, savepath_black)
        except:
            error_list.append(paths)
            print(paths + ' is lost.')






    # save all the features
    feature_list.sort()
    fi = open(os.path.join(featuresave,'features') + '.txt','w')
    for line in feature_list:
        fi.write(line)
        fi.write('\n')
    fi.close()

    print(len(error_list),'\n',error_list)
    print(len(feature_list))

    time2 = time()

    print('The cost time is ',(time2-time1)/60,' min.')