#################################Network_Programming - MileStone_Project_2###########################
#TCP/UDP Port Scanner using Scapy and argeparse
# __author__ = "Srivaishnavi"
# Version = 1.0
#Created = 11/2/2022
#TCP/UDP port scanning by passing "input" dynamically using arg_parse library.

import pyfiglet
import argparse
from scapy.all import *

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# argeparse argument setup
parser = argparse.ArgumentParser("Port scanner using Scapy")
parser.add_argument("-t", "--target_IP", help="Specify target IP", required=True)
parser.add_argument("-p", "--ports", type=int, nargs="+", help="Specify the port number(21 23 80 ...)")
parser.add_argument("-s", "--scan_type", help="Scan type, syn/udp/xmas", required=True)
args = parser.parse_args()

# argparse mapping
target_IP = args.target_IP  # App takes IP or IP range as one argument by using argeparse
scan_type = args.scan_type.lower()
# set ports only if passed
if args.ports:
    ports = args.ports  # App takes a port or list of ports to scan
else:
    # setting the default port range
    ports = range(1, 1024)

# scan_types declaration    #App takes the type of scan to perform as an argument
if scan_type == "syn" or scan_type == "s":  # TCP-SYN, TCP-ACK scan_type
    syn_scan(target_IP, ports)
elif scan_type == "udp" or scan_type == "u":  # UCP port scan_type
    udp_scan(target_IP, ports)
elif scan_type == "xmas" or scan_type == "x":  # FTU just tried to do something apart from just TCP/UDP
    xmas_scan(target_IP, ports)
else:
    print("Scan type not supported")

# formatting the output
def print_ports(port, state):
    print("%s | %s" % (port, state))

def main():
    # Scan code function for TCP-SYN, TCP-ACK options
    def syn_Ack_scan(target_IP, ports):
        print("syn scan on, %s with ports %s" % (target_IP, ports))

    sport = RandShort()
    for port in ports:
        pkt = sr1(IP(dst=target_IP) / TCP(sport=sport, dport=port, flags="S"), timeout=1, verbose=0)
        if (str(type(pkt) == "<type 'Nonetype'>")):
            if (pkt.haslayer(TCP)):
                tcplayer = pkt.getlayer(TCP).flags
                print(f" Printing the tcplayer flag mapping {tcplayer}")
                if (
                        tcplayer == 0x12):  # The hexadecimal equivalent of syn,ack (can be done using 18, 20 flags) we get, when port is open
                    print_ports(port, "Closed")
                elif (tcplayer == 0x14):  # The hexadecimal equivalent of rst,ack we get, when port is closed
                    print_ports(port, "Open")
                else:
                    print_ports(port, "TCP packet resp / filtered")
            elif (pkt.haslayer(ICMP)):
                print_ports(port, "ICMP resp / filtered")
            else:
                print_ports(port, "Unknown resp")
                print(pkt.summary())
    else:
        print_ports(port, "Unanswered")

# Scan code function for UDP option
def udp_scan(target_IP, ports):
    print("udp scan on, %s with ports %s" % (target_IP, ports))
    for port in ports:
        pkt = sr1(IP(dst=target_IP) / UDP(sport=port, dport=port), timeout=2, verbose=0)
        if (str(type(pkt) == "<type 'Nonetype'>")):
            print_ports(port, "Open / filtered")
        else:
            if pkt.haslayer(UDP):
                print_ports(port, "Open / filtered")
            elif pkt.haslayer(ICMP):
                print_ports(port, "Closed")
            else:
                print_ports(port, "Unknown")
                print(pkt.summary())

if __name__ == "__main__":
    main()