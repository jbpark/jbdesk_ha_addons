from fabric.api import *
from fabric.api import sudo, settings

def get_os_version(gateway, host_string, user, password, passwords):
    with settings(gateway="%s" % gateway, host_string="%s" % host_string, user="%s" % user,
                  password="%s" % password, passwords=passwords, warn_only=True):
        with hide('output', 'warnings', 'running'):
            res = sudo('rpm -qa *-release', shell=False)
            os_version = None
            if res.find('centos-release-') == -1:
                print('OS Version : Not Found')
            else:
                for line in res.splitlines():
                    line = line.strip()
                    if line.find('centos-release-') == -1:
                        continue

                    items = line.split('.')
                    os_string = items[0]
                    os_version = os_string[15:]
                    os_version = os_version.replace("-", ".")

            return os_version

def get_os_version_without_gateway(host_string, user, password):
    with settings(host_string="%s" % host_string, user="%s" % user,
                  password="%s" % password, warn_only=True):
        with hide('output', 'warnings', 'running'):
            res = sudo('rpm -qa *-release', shell=False)
            os_version = None
            if res.find('centos-release-') == -1:
                print('OS Version : Not Found')
            else:
                for line in res.splitlines():
                    line = line.strip()
                    if line.find('centos-release-') == -1:
                        continue

                    items = line.split('.')
                    os_string = items[0]
                    os_version = os_string[15:]
                    os_version = os_version.replace("-", ".")

            return os_version
