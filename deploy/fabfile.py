# deployment of salt-minions

import os
from fabric.contrib import files
from fabric.api import env, sudo, put, task, roles
from fabric.colors import red
from ConfigParser import ConfigParser

work_path = os.path.dirname( __file__ )
cfg_name = '/salt_deploy.cfg'
cfg_file = work_path + cfg_name
if not os.path.isfile(cfg_file ):
    print red("Missing config file. (%s)" % cfg_name)
    os.sys.exit()

env.config = ConfigParser()
env.config.read(cfg_file)
env.user = env.config.get('ENV','user')
env.password = env.config.get('ENV','password')
env.roledefs['MASTER']= env.config.get('ENV','master')
env.roledefs['MINION']= env.config.get('ENV','minion')
env.roledefs['ALL']= env.roledefs['MASTER'] + env.roledefs['MINION']

@task
def deploy():
    '''
        deploy Saltstack based on configuration in salt_deploy.cfg
    '''
    if len(env.roledefs['ALL']) > 0:
        deploy_pre()

    if len(env.roledefs['MASTER']) > 0:
        deploy_master()

    if len(env.roledefs['MINION']) > 0:
        deploy_minion()

@task
@roles('MASTER')
def deploy_master():
    deploy_salt("master")

@task
@roles('MINION')
def deploy_master():
    deploy_salt("minion")


@task
@roles('ALL')
def deploy_pre():
    '''
        Saltstack deployment pre requisites
    '''
    sudo('apt-get -y install python-software-properties')
    sudo('add-apt-repository -y ppa:saltstack/salt')
    sudo('apt-get update')

@task
def deploy_salt(salt_services):
    '''
        Deploy salt services

        takes as argument list of services to install, split in comma
        ie, "master,minion"
    '''

    service_list = salt_services.split()

    for service in service_list:
        if service in ['minion', 'master']:
            install_salt(service)
            config_salt(service)
            restart_salt_service(service)
        else:
            print red("ERROR: incorrect salt service specified: %s" % service)

@task
def install_salt(service_name):
    '''
        Install salt-minion package
    '''
    cmd_line = 'apt-get -y install salt-%s' % service_name
    sudo(cmd_line)

@task
def restart_salt_service(service_name):
    '''
        Restart salt services
    '''
    cmd_line = 'service salt-%s restart' % service_name
    sudo(cmd_line )

@task
def config_salt(service_name):
    '''
        Configure salt

        takes as argument the configuration file name
        valid names are master and minion
    '''
    remote_path = '/etc/salt/%s' % service_name
    put(service_name, remote_path, use_sudo=True, mode=0644)

