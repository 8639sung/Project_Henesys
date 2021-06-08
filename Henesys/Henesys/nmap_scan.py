from django.contrib.auth.models import User
from accounts.models import HenesysUser 
from django.http import request
import nmap
import os
from getmac import get_mac_address

def scan():
    nm = nmap.PortScanner()
    online_user_list = []

    scan_range = nm.scan(hosts='192.168.0.1/24', arguments='-sn -PI -PT')
    live_hosts_list = [get_mac_address(ip=x) for x in nm.all_hosts()]
    print(live_hosts_list)
    user_list = HenesysUser.objects.all()
    for live_host in live_hosts_list :
        for user in user_list :
            if user.mac_address == live_host :
                online_user_list.append(user.username)     
    return online_user_list

def get_client_ip(request):
    x_forwarded_for = request.META['HTTP_X_FORWARDED_FOR']
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META['REMOTE_ADDR']
    return ip

def get_my_mac():
    visitor_ip = get_client_ip(request)
    mac = get_mac_address(ip=visitor_ip)
    return mac