
# stdlib
import os
import re
import syslog
import json
from json import JSONEncoder

# 3rd party
from ConfigParser import SafeConfigParser
import requests
from jsonmerge import merge

#own libraries
import system

# Getting data from the configuration file

parser = SafeConfigParser()
parser.read('dstack-agent.conf')


ip = parser.get('apiserver', 'ip')
port = parser.get('apiserver', 'port')

print ip,port

x = system.SystemInfo()

sysinfo= x.getsystem_info()
sysmem= x.getsystem_memory()

data=[sysmem,sysinfo]

print json.dumps(data, ensure_ascii=False)

def api_version():
	r = requests.get('http://%s:%s/api/info'%(ip,port))
	print r.status_code

api_version()


#if __name__ == "__main__":
