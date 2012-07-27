base:

  'roles:wilog':
    - match: grain
    - packages.java.openjdk-7-jre-headless
    - packages.python.python-pip
    - packages.scm.git
  
  'roles:mongodb':
    - match: grain
    - packages.nosql.mongodb

