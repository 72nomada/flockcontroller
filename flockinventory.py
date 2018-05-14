# flock inventory
# v0.0 14-05-18 master@owlh.net

import flockdefs
import json
import flocklogger 

flogger = flocklogger.flocklogger


def loadinventory():
    with open(flockdefs.inventory) as json_data:
        owlhs = json.load(json_data)
        print len(owlhs)
    return owlhs

def printinventory(owlhs):
    for owlh in owlhs: 
        print owlh["name"]


