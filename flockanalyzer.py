#flock analyzer 
#v0.0 21.05.18 master@owlh.net

#    "owlh_interface" : "owlh",
#    "suricata_on" : "True",
#    "bro_on" : "True"
#   ·"safe_pcap_locally" : "True"

# lsof must be in place or Python-Lsof is possible? 
# psutil must be in place. pip install psutil >>> Seems to not be useful as we think
# 

def disposal_pcap (pcap):
    #if send remote
        # send remote
    #if any failure or save_pcap_locally
        #mv pcap to pcap_out_queue(pcap)
    #if delete local
        # remove local

def pcap_ready (pcap): 
    ready = False
    # check lsof python
    # not open pcap >> ### lsof /home/jose/openrules.pcap
    return ready

def put_in_progress (pcap):
    #mv pcap from pcap_in_queue to pcap_in_progress

def manage_pcap (pcap):
    #if pcap_ready(pcap)
        #put_in_progress(pcap)
        #run tcpreplay over owlh interface
        #disposal pcap
        #exit 
    # log that file is still open

def read_pcaps():
    pcaps = []
    #read pcaps from folder - just the name.
    return pcaps

def main ():
    #read conf
    #verify suricata is "ON" or bro is "ON" (as per configuration)
    #while True:
        #pcaps = read_pcaps()
        #for pcap in pcaps:
            #fork? As this is traffic, should be find to have traffic from different pcaps mixed. 
