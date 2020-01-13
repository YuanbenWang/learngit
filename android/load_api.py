import os
import re
import numpy as np
from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm
from androguard.core.analysis import analysis

if __name__ == '__main__':
    filename = r'F:\360.apk'
    app = apk.APK(filename)
    app_dex = dvm.DalvikVMFormat(app.get_dex())
    app_x = analysis.newVMAnalysis(app_dex)
    methods = set()

    cs = [cc.get_name() for cc in app_dex.get_classes()] # return all the classes' name

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
                    index1= line.find('>')
                    index2= line.find('(')
                    line = line[index1+1:index2]
                    methods.add(line)

    methods = list(methods)
    methods.sort()

