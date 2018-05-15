#!/usr/bin/env python3

# owlh controller
# v0.0 14.05.18 master@owlh.net

import time
import os
import sys

# own libs
import flocklogger 
import flockmanager
import flockinventory
import flockconf

flogger = flocklogger.flocklogger
flocklogger.initflocklogger()


def main():
    if not flockmanager.amirunning():
        while not flockmanager.killme():
            flockmembers = flockinventory.loadinventory()
            flockinventory.printinventory(flockmembers)
            fconf = flockconf.loadconf()
            flockconf.printconf(fconf) 
            time.sleep (10) # Just for testing, deleting in a while
        flockmanager.byebye()

main()