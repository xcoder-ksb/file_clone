import os,platform
os.system('git pull')
os.system('pip uninstall requests')
os.system('pip install requests')
x=platform.architecture()[0]
if x=="32bit":
    import bit

elif x=="64bit":
    import file_clone
