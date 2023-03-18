import os,platform
os.system('git pull')
 
trt=platform.architecture()[0]
if trt=="32bit":
    from 32 import menu_apikey
elif trt=="64bit":
    import file
