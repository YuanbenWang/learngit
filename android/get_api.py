__author__ = 'Administrator'
#coding=utf-8
from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
global count
count = 2

def get_apis(path, filename):
  app = apk.APK(path)
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
  str = "Methods:"
  file = methods
  # writeToTxt(str, file, filename)
  return methods

def writeToTxt(str, file, filename):
    global count
    fm = open('%d'%count+'.txt', 'w')
    #fm.write(str)
    #fm.write("\n")
    for i in file:
        tmp = i.split('.')
        final = tmp[-1]
        fm.write(final)
        fm.write("\n")
    fm.close()
    count += 1

if __name__ == '__main__':
    path = r"/home/huu/Downloads/apks/2.apk"
    filename = "sampleInfo.txt"
    apis = get_apis(path, filename)
    print (apis)
