#!/usr/bin/env python3

# owlh controller
# v0.0 14.05.18 master@owlh.net

import time
import os.path
import signal

# own libs
import flocklogger 
import flockdefs
import flockkiller

flogger = flocklogger.flocklogger
killer = flockkiller.flockKiller()

def registerflock():
    flogger (str(os.getpid()))
    file(flockdefs.pidfile, 'w').write(str(os.getpid()))

def amirunning():
    if os.path.isfile(flockdefs.pidfile):
        flogger ("I'm running, we don't need two of us, exiting...")
        flogger ("If you think I'm not running, please check proc and " + flockdefs.pidfile)
        return True
    registerflock()
    return False

def byebye():
    flogger ("Time to go home. See you soon")
    os.unlink(flockdefs.pidfile)

def main():
    if not amirunning():
        while not killer.killme:
            flocklogger.flocklogger("hellowl")
            print "hellowl!"
            time.sleep (30)
        byebye()

main()