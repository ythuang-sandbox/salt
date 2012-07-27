# deployment of salt-minions

from fabric.contrib import files


env.user = 'setusername'
env.password = 'setpassword'
env.hosts = []

def deploy_pre():
    install_py_soft_properties()
    add_saltstack_ppa()
    update_repo()

def deploy_salt_master():
    deploy_pre()
    install_salt_master()
    config_salt_master()

def deploy_salt_minion():
    deploy_pre()
    install_salt_minion()
    config_salt_minion()


def install_py_soft_properties():
    '''
        install python-software-properties software package
    '''
    sudo('apt-get -y install python-software-properties')

def add_saltstack_ppa():
    '''
        add saltstack ppa
    '''
    sudo('add-apt-repository -y ppa:saltstack/salt')

def update_repo():
    '''
        update the repository
    '''
    sudo('apt-get update')

def install_salt_minion():
    '''
        install salt-minion package
    '''
    sudo('apt-get install salt-minion')

def install_salt_master():
    '''
        install salt-master package
    '''
    sudo('apt-get install salt-master')

def config_salt_minion():
    '''
        configure salt-minion
    '''
    fabric.operations.put('minion','/etc/salt/minion',use_sudo=True,mode=0644)

def config_salt_master():
    '''
        configure salt-master
    '''
    fabric.operations.put('master','/etc/salt/master',use_sudo=True,mode=0644)
