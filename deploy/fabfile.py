# deployment of salt-minions

env.user = 'setusername'
env.password = 'setpassword'
env.hosts = []

def deploy():
    install_py_soft_properties()
    add_saltstack_ppa()
    update_repo()
    install_salt_minion()


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

def config_salt_minion():
    '''
        configure salt-minion
    '''
    