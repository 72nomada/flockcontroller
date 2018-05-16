#flock monitor
#v0.0 16-05-18 master@owlh.net

import flocklogger

flogger = flocklogger.flocklogger

def check_owl_alive (owl):
    flogger ("check owl %s is alive" % owl["name"])

def get_status_cpu (owl):
    flogger ("check owl %s CPU" % owl["name"])

def get_status_mem (owl):
    flogger ("check owl %s MEM" % owl["name"])

def get_status_storage (owl):
    flogger ("check owl %s storage" % owl["name"])

def get_status_sniffer (owl):
    flogger ("check owl %s sniffer status" % owl["name"])

def run_sniffer (owl):
    flogger ("run sniffer on owl %s" % owl["name"])

def stop_sniffer (owl):
    flogger ("stop sniffer on owl %s" % owl["name"])

def get_file_list (owl):
    flogger ("get file list on owl %s" % owl["name"])

def transport_file (owl, file):
    flogger ("get file %s from owl %s" % (file, owl["name"]))

def remove_file (owl, file):
    flogger ("remove file %s from owl %s" % (file, owl["name"]))
