# deployment of salt-minions

from fabric.contrib import files
from fabric.api import env, sudo, put
from fabric.colors import red

env.user = 'setusername'
env.password = 'setpassword'
env.hosts = []

def deploy_pre():
    '''
        Saltstack deployment pre requisites
    '''
    sudo('apt-get -y install python-software-properties')
    sudo('add-apt-repository -y ppa:saltstack/salt')
    sudo('apt-get update')


def deploy_salt(salt_services="minion"):
    '''
        Deploy salt services

        takes as argument list of services to install, split in comma
        ie, "master,minion"
    '''
    deploy_pre()

    service_list = salt_services.split()

    for service in service_list:
        if service in ['minion', 'master']:
            install_salt(service)
            config_salt(service)
        else:
            print red("ERROR: incorrect salt service specified: %s" % service)


def install_salt(service_name):
    '''
        Install salt-minion package
    '''
    cmd_line = 'apt-get install salt-%s' % service_name
    sudo(cmd_line)


def config_salt(service_name='minion'):
    '''
        Configure salt

        takes as argument the configuration file name
        valid names are master and minion
    '''
    remote_path = '/etc/salt/%s' % service_name
    put(service_name, remote_path, use_sudo=True, mode=0644)

