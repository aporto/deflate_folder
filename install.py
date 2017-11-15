#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alex
#
# Created:     06/10/2017
# Copyright:   (c) alex 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys


reg_text = '''Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\shell\deflate_folder_shell_command]
@="Deflate folder"

[HKEY_CLASSES_ROOT\Directory\shell\deflate_folder_shell_command\command]
@="\\"{}\\" \\"%1\\""
'''

def register_context_menu(application_path):
    global reg_text
    print "Install will launch regedit to register the Context menu..."

    path = application_path
    path = os.path.join(path, 'windows', 'deflate_folder.bat')
    path = path.replace('\\', '\\\\')

    reg_text = reg_text.format(path)

    fname = application_path
    fname = os.path.join(fname, 'windows', 'register_context_menu_for_deflate_folder.reg')
    with open(fname, 'w') as f:
        f.write(reg_text)

    #os.system("pause")
    os.system("start "+fname)
    #os.remove(fname)

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
    #print "Running from PyInstaller"
else:
    #print "Running from Python.exe"
    application_path = os.path.dirname(os.path.abspath(__file__))

application_path = os.path.abspath(os.path.join(application_path, '..'))


print "************************************************************************"
print "Installing Deflate Folder context menu..."
print ""

register_context_menu(application_path)

print ""
print "Installation finished!"
print "************************************************************************"

os.system("pause")
