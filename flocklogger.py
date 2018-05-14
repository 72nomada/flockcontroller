
# flock logger 
# v0.0 14.05.18 master@owlh.net

import os
import flockdefs

logfile = ""

def initflocklogger():
    global logfile 
    bufsize = 0 # 0 -> force flush on each write
    logfile = file(flockdefs.logfile,'a',bufsize)

def killflocklogger():
    global logfile
    logfile.close()

def flocklogger(text):
    print ">>> " + text
    global logfile
    logfile.write(">>> " + text + "\n")
