import os,platform
os.system('git pull')
 
trt=platform.architecture()[0]
if trt=="32bit":
    __import__("bit")
elif trt=="64bit":
    import file_clone
