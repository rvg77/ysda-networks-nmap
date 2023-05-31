import sys
from scapy.config import conf
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1
import argparse
from tqdm.auto import trange

def port_is_closed(host, port):
    response = sr1(IP(dst=host)/TCP(dport=port, flags='S'), verbose=0, timeout=1)
    return response is None or response.getlayer(TCP).flags != 'SA'
    
def scan_ports(host: str, ports_start: int, ports_finish: int):    
    conf.verb = 0
    return [port for port in trange(ports_start, ports_finish) if port_is_closed(host, port)]
    
def parse_args():
    parser = argparse.ArgumentParser(description='Nmap analogue.')
    
    parser.add_argument('host', help='destination host address')
    parser.add_argument('ports', type=str, help='Ports range to scan, e.g. 1-100', default='1-100')
    
    args = parser.parse_args()
    
    args.ports = list(map(int, args.ports.split('-')))

    return args

if __name__ == '__main__':
    args = parse_args()
    
    closed_ports = scan_ports(args.host, args.ports[0], args.ports[1])
    
    for p in closed_ports:
        print(f"Port {p}: CLOSED")
