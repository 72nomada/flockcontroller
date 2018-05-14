#!/usr/bin/env python3

# owlh controller
# v0.0 14.05.18 master@owlh.net

import time

# own libs
import flocklogger 
import flockmanager

flogger = flocklogger.flocklogger

def main():
    if not flockmanager.amirunning():
        while not flockmanager.killme():
            flogger("hellowl")
            print "hellowl!"
            time.sleep (30)
        flockmanager.byebye()

main()