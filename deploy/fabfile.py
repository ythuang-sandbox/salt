# deployment of salt-minions

from fabric.contrib import files
from fabric.api import env, sudo

env.user = 'setusername'
env.password = 'setpassword'
env.hosts = []

def deploy_pre():
    '''
        Saltstack deployment pre requisites
    '''
    install_py_soft_properties()
    add_saltstack_ppa()
    update_repo()

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
            print fabric.colors.red("ERROR: incorrect salt service specified: %s" % service )

def install_py_soft_properties():
    '''
        Install python-software-properties software package
    '''
    sudo('apt-get -y install python-software-properties')

def add_saltstack_ppa():
    '''
        Add saltstack ppa
    '''
    sudo('add-apt-repository -y ppa:saltstack/salt')

def update_repo():
    '''
        Update the repository
    '''
    sudo('apt-get update')

def install_salt(service_name):
    '''
        Install salt-minion package
    '''
    cmd_line = 'apt-get install salt-%s' % service_name
    sudo(cmd_line)


def config_salt(service_name = 'minion'):
    '''
        Configure salt

        takes as argument the configuration file name
        valid names are master and minion
    '''
    remote_path = '/etc/salt/%s' % service_name
    fabric.operations.put(service_name,remote_path,use_sudo=True,mode=0644)

