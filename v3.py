import os,platform
os.system('git pull')
 
trt=platform.architecture()[0]
if trt=="32bit":
    import 32
elif trt=="64bit":
    import file
