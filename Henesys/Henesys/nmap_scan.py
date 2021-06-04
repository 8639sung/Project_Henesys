import nmap
from getmac import get_mac_address

def scan():
    nm = nmap.PortScanner()

    scan_range = nm.scan(hosts='192.168.0.1/24', arguments='-sn -PI -PT')
    hosts_list = [get_mac_address(ip=x) for x in nm.all_hosts()]

    return hosts_list

def get_my_mac():
    mac = get_mac_address()
    return mac