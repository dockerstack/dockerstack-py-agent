#stdlib
import os
import logging
 
#3rd Party lib
import psutil
 
#Logging Class Initialization
 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
 
 
class ServiceCheck(object):

	def  is_docker_running(self,process_name="docker"):
		for proc in psutil.process_list():
			if proc.name != process_name:
				continue
			else:     
				return True