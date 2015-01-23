#import syslog
import logging
from docker import Client
 
 
#Logging Class Initialization
 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
 
# Docker Client Base URL
c = Client(base_url='unix://var/run/docker.sock')
 
 
class DockerSystemInfo():
 
    def docker_get_version(self):
        """
        Get the Docker Service Version Information
        Installed on the Server
        """
        try:
            return c.version()
        except Exception, e:
            logger.info(e)
       
 
    def docker_image_list(self):
        return "Hello World"
 
    def docker_running_containers(self):
        """
        Will get the information about the running
        containers on the Server
        """
        try:
            return c.containers()
        except Exception, e:
            logger.info(e)
        return "Hello World"
 
    def docker_container_start(self):
        return "Hello World"
 
    def docker_container_remove(self):
        return "Hello World"