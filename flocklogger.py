
# flock logger 
# v0.0 14.05.18 master@owlh.net

import os
import flockdefs
from datetime import datetime


logfile = ""

def initflocklogger():
    global logfile 
    bufsize = 0 # 0 -> force flush on each write
    logfile = file(flockdefs.logfile,'a',bufsize)

def killflocklogger():
    global logfile
    logfile.close()

def flocklogger(text, proc="flock", id=os.getpid()):
    print ">>> " + text
    global logfile
    logfile.write(datetime.utcnow().strftime('%a %d %b %Y %H:%M:%S.%f') + " [" + proc + "] (" + str(id) +"): " + text + "\n")
