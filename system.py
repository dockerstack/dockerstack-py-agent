# stdlib
import platform
import json
import os
import socket
import multiprocessing
from json import JSONEncoder
import fcntl
import struct

# 3rd Party
import psutil


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True


def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
        ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip


class SystemInfo():

    def getsystem_info(self):

        processor = platform.uname()[5]
        plat = platform.platform()
        os_name = platform.uname()[0]
        os_version = platform.uname()[2]
        arctype = platform.architecture()[0]
        system = platform.system()
        cpus = multiprocessing.cpu_count()
        ip = get_lan_ip()

        data = {
            "ip": ip, 
            "processor": processor,
            "arc": arctype, 
            "cpus": cpus,                       
            "os": os_name,
            "os_version": os_version
                        
        }
       
        return data

    def getsystem_memory(self):
        """
        Will get the System memory of the server
        """
        totalmem = psutil.phymem_usage()[0]
        freemem = psutil.avail_phymem()
        usedmem = psutil.used_phymem()

        data = {
            "total": str(totalmem),
            "free": str(freemem),
            "used": str(usedmem)
            
        }
        
        return data

    def getsystem_disk_usage(self):
        return "Hello"


