# flock conf
# v0.0 14-05-18 master@owlh.net

configfile = "conf.json" # this must be in other place.

import json
import flocklogger 

flogger = flocklogger.flocklogger


def loadconf():
    with open(configfile) as conf_data:
        conf = json.load(conf_data)
        print len(conf)
    return conf

def printconf(conf):
    for item in conf: 
        print item