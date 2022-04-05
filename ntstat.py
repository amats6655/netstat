from os import popen
from platform import system
from datetime import datetime

date_now = str(datetime.today().strftime("%d%m%Y_%H%M%S"))
ping_ip1 = "1.1.1.1"
ping_ip2 = "8.8.8.8"
oc = system()


def get_adapters():
    print("GET ADAPTERS")
    txt = ""
    if oc == "Windows":
        adapters = "netsh interface ip show interface"
    else:
        adapters = "ip -br address"
    response = popen(adapters)
    for adapter in response.readlines():
        txt += adapter
    if oc == "Windows":
        response = popen("netsh interface ip show addresses")
        for adapter in response.readlines():
            txt += adapter
    return txt


def get_dns():
    print("GET DNS")
    txt = ""
    if oc == "Windows":
        dnss = "netsh interface ip show dnsservers"
    else:
        dnss = "nmcli dev show | grep DNS"
    response = popen(dnss)
    for dns in response.readlines():
        txt += dns
    return txt


def get_ssid():
    print("GET SSID")
    txt = ""
    if oc == "Windows":
        ssids = 'netsh wlan show interface | findstr "SSID"'
    else:
        ssids = 'nmcli dev wifi list'
    response = popen(ssids)
    for ssid in response.readline():
        txt += ssid
    return txt


def get_ping(ip):
    print("GET PINGS " + ip)
    txt = ""
    if oc == "Windows":
        ping = "ping -n 4 "
    else:
        ping = "ping -c 4 "
    response = popen(ping + ip)
    for ping in response.readlines():
        txt += ping
    return txt


def get_route():
    print("GET ROUTING")
    txt = ""
    if oc == "Windows":
        routee = "netsh interface ip show route"
    else:
        routee = 'routel'
    response = popen(routee)
    for route in response.readlines():
        txt += route
    return txt


net_file = open("ntstat_" + date_now + ".log", "w+")
net_file.write("=========================== ADAPTERS ===========================\n" + get_adapters().encode('cp1251').decode('cp866'))
net_file.write("\n\n============================= DNS =============================\n\n" + get_dns().encode('cp1251').decode('cp866'))
net_file.write("\n\n============================= SSID =============================\n\n" + get_ssid().encode('cp1251').decode('cp866'))
net_file.write("\n\n====================== PING " + ping_ip1 + " ======================\n\n" + get_ping(ping_ip1).encode('cp1251').decode('cp866'))
net_file.write("\n\n====================== PING " + ping_ip2 + " ======================\n\n" + get_ping(ping_ip2).encode('cp1251').decode('cp866'))
net_file.write("\n\n============================= ROUTE =============================\n\n" + get_route().encode('cp1251').decode('cp866'))
net_file.close()
