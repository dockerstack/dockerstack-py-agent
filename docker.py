# import syslog
import logging
from docker import Client


# Logging Class Initialization

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    value = "sock"
    dockerurl = parser.get('main', 'docker_url')
    dockerport = parser.get('main', 'docker_port')
    if re.search("(so.*)", value) in docker_url:
        c = Client(base_url=dockerurl)
    else:
        c = Client(base_url="http://%s:%s" % (dockerurl, dockerport)
except Exception, e:
    logger.debug(e)


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
        """
        Get the List of images available in the local Registry
        """
        try:
            return c.images()
        except Exception, e:
            logger.debug(e)

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
