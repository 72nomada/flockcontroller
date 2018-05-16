# flock inventory
# v0.0 14-05-18 master@owlh.net

import flockdefs
import json
import flocklogger 
import flockmonitor

flogger = flocklogger.flocklogger


def loadinventory():
    with open(flockdefs.inventory) as json_data:
        owlhs = json.load(json_data)
        print len(owlhs)
    return owlhs

def printinventory(owlhs):
    for owlh in owlhs: 
        print owlh["name"]

def run():
    owls = loadinventory()
    for owl in owls: 
        flogger("checks for owl name -> %s, owl ip -> %s" % (owl["name"], owl["ip"]))
        flockmonitor.get_status_cpu(owl)
        flockmonitor.remove_file(owl, "pcap.file")


