#!/usr/bin/env python3

# owlh controller
# v0.0 14.05.18 master@owlh.net

import time

# own libs
import flocklogger 
import flockmanager

flogger = flocklogger.flocklogger
flocklogger.initflocklogger()


def main():
    if not flockmanager.amirunning():
        while not flockmanager.killme():
            flogger("hellowl") # remove from here. it make not sense here
            print "hellowl!" # remove from here. it make not sense here
            time.sleep (30) # Just for testing, deleting in a while
        flockmanager.byebye()

main()