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
import fnmatch
#import subprocess
import shutil
#import re
#import difflib
#import json
import time
#import datetime

exclude_files = [
    '*.txt',
    '*.jpg','*.png',
    '*.nfo'
]


def deflate_folder(path, initial_path = "", non_deflated = ""):
    if initial_path == "":
        non_deflated = os.path.join(path, 'non_deflated')
        if not os.path.isdir(non_deflated):
            os.makedirs(non_deflated)
        initial_path = path
    else:
        print "\t" + path
    dirs = os.listdir(path)
    for d in dirs:
        full_path = os.path.join(path, d)
        if os.path.isdir(full_path):
            if full_path != non_deflated:
                deflate_folder(full_path, initial_path, non_deflated)
                shutil.rmtree(full_path)
        else:
            dest = os.path.join(initial_path, d)
            ignore_this_file = False
            for ignore in exclude_files:
                if fnmatch.fnmatch(d.lower(), ignore.lower()):
                    ignore_this_file = True
                    break
            if ignore_this_file:
                print "\t\tIgnoring %s (Moving it to 'non_deflated' folder)" % (d)
                shutil.move(full_path, os.path.join(non_deflated, d))
            else:
                if dest != full_path:
                    print "\t\tMoving %s to initial dir" % (d)
                    shutil.move(full_path, dest)
    return non_deflated


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python deflate_folder.py <PATH>..."
    else:
        path = ' '.join(sys.argv[1:])
        print "Deflating:", path
        non_deflated = deflate_folder(path)
        if len(os.listdir(non_deflated)) == 0:
            shutil.rmtree(non_deflated)
        print "Done!"

