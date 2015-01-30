
# stdlib
import os
import re
import syslog
import json
import time
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

jsondata={"root":"/opt","folder":"dockerstack.github.io"}

ip = parser.get('apiserver', 'ip')
port = parser.get('apiserver', 'port')

polling = parser.get('main','polling')
polling_time = parser.get('main','polling_time')

jsondata={"root":"/opt","folder":"dockerstack.github.io"}

class DockerAgent():	

	def api_version(self):
		r = requests.get('http://%s:%s/api/info'%(ip,port))
		print r.status_code
		print r.text

	def post_ServerData(self,jsondata):

		try:
			url = 'http://%s:%s/api/filefetch/readdir/folder'%(ip,port)
			r = requests.post(url, data=json.dumps(jsondata))
			print r.text
		except Exception,e:
			print e

def main():
	while True:
		app = DockerAgent()
		app.api_version()
		app.post_ServerData(jsondata)

		time.sleep(int(polling_time))


if __name__ == "__main__":
	
	main()