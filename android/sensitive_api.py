from androguard.core.bytecodes import apk, dvm
from androguard.core.analysis import analysis
import re
import os
from time import time

def show_Sensitive_APIs(dx):
    for i in Sensitive_APIs:
        print (" ",i,Sensitive_APIs[i][0],Sensitive_APIs[i][1])
        paths = dx.get_tainted_packages().search_methods( Sensitive_APIs[i][0],Sensitive_APIs[i][1],".")
        show_Paths(dx.get_vm(), paths )
Sensitive_APIs = {
    #log
    #0 : [ "Landroid/util/Log;","d"],
    #send sms
    1: ["Landroid/telephony/SmsManager;","sendTextMessage"],
    #read sms
    2: [".","getDisplayMessageBody"],
    3: [".","getMessageBody"],
    #IMEI
    4: ["Landroid/telephony/TelephonyManager;","getDecicedID"],
    #phone number
    5: ["Landroid/telephony/TelephonyManager;","getLine1Number"],
    #get Sim serial
    6: ["Landroid/telephony/TelephonyManager;","getSimSerialNumber"],
    #Location
    7: ["Landroid/telephony/TelephonyManager;","getCellLocation"],
    #GPS
    8: [".","getLastKnownLocation"],
    9: [".","requestLocationUpdates"],
    #Recorder
    10: ["Landroid/media/MediaRecorder;","prepare"],
    #native_code
    11: ["Ljava/lang/Runtime;","exec"],
    12: ["Ljava/lang/Runtime;","load"],
    13: ["Ljava/lang/System;","load"],
    #file io
    14: ["Llibcore/io/IoBridge;", "open"],
    15: ["Llibcore/io/IoBridge;", "read"],
    16: ["Llibcore/io/IoBridge;", "write"],
    17: ["Ljava/io/File;", "create"],
    18: ["Ljava/io/File;", "delete"],
    19: ["Ljava/io/File;", "get"],
    20: ["Ljava/io/File;", "mk"],
    21: ["Ljava/io/File;", "set"],
    #get resource
    22: [".","openRawResource"],
    23: [".","getAssets"],
    #http
    24: ["Lorg/apache/http/impl/client/AbstractHttpClient;", "execute"],
    25: ["Ljava/net/HttpURLConnection;","connect"],
    26: ["Ljava/net/URL;","openConnection"],
    27: ["Ljava/net/URLConnection;","connect"],
    28: ["Ljava/net/Socket;","."],
    #ssl
    29: ["Ljavax/net/ssl;","."],
    #WebView
    30: ["Landroid/webkit/WebView;","addJavascriptInterface"],
    31: ["Landroid/webkit/WebView;","searchBoxJavaBridge_"],
    #load jar
    32: ["Ldalvik/system/DexClassLoader;","."],
    33: ["Ljava/net/URLClassLoader;","."],
    34: ["Ldalvik/system/PathClassLoader;","."],
    #ReflectionCode
    35: ["Ljava/lang/reflect/Method;", "."],
    #encrypt or SHA
    36: [".", "doFinal"],
    37: [".","digest"],
    #use camera
    38: ["Landroid/hardware/Camera;","open"],
    #query SQL(read contact\SMS)
    39: ["Landroid/content/ContentResolver;","query"],
    #SharedPreferences
    40: ["Landroid/content/SharedPreferences;","edit" ],
    #sendBroadcast
    41: [".","sendBroadcast"],
    42: [".","sendOrderedBroadcast"],
    43: [".","sendStickyBroadcast"],
    44: [".","sendStickyOrderedBroadcast"],
    #start activity
    45: [".","startActivity"],
    46: [".","startActivityForResult"],
    #Service
    47: [".","startService"],
    48: [".","bindService"],
    #write to SD card ,add by Colbert 20150120
    49: [".","getExternalStorageDirectory"],
    #input check ,add by Colbert 20150120
    50: [".","readLine"]
}