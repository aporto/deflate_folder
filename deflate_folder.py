#-------------------------------------------------------------------------------
# Name:        Deflate Folder
# Purpose:
#
# Author:      Alex Porto
#
# Created:     27/09/2017
# Copyright:   (c) Alex Porto 2017
# Licence:     GPLv3
#-------------------------------------------------------------------------------

import os, sys
#import subprocess
import shutil
#import re
#import difflib
#import json
import time
#import datetime


def deflate_folder(path, initial_path = ""):
    if initial_path == "":
        initial_path = path
    else:
        print "\t" + path
    dirs = os.listdir(path)
    for d in dirs:
        full_path = os.path.join(path, d)
        if os.path.isdir(full_path):
            deflate_folder(full_path, initial_path)
            shutil.rmtree(full_path)
        else:
            dest = os.path.join(initial_path, d)
            if dest != full_path:
                print "\t\tMoving %s to initial dir" % (d)
                shutil.move(full_path, dest)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python deflate_folder.py <PATH>..."
    else:
        path = sys.argv[1]
        print "Deflating:", path
        deflate_folder(path)
        print "Done!"

