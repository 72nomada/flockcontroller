
# flock logger 
# v0.0 14.05.18 master@owlh.net

import os
import flockdefs
from datetime import datetime


def initflocklogger():
    global logfile 
    bufsize = 0 # 0 -> force flush on each write
    logfile = file(flockdefs.logfile,'a',bufsize)

def killflocklogger():
    flocklogger ("Closing log output")
    global logfile
    logfile.close()

def flocklogger(text, level="INFO", proc="flock", id=os.getpid()):
    global logfile
    logfile.write(datetime.utcnow().strftime('%a %d %b %Y %H:%M:%S.%f') + " [" + proc + "] (" + str(id) +") [" + level+ "]: " + text + "\n")

logfile = ""
initflocklogger()
