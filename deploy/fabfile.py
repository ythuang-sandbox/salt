# deployment of salt-minions

def deploy():
  sudo('apt-get -y install python-software-properties')
  sudo('add-apt-repository -y ppa:saltstack/salt')
  sudo('apt-get update')


