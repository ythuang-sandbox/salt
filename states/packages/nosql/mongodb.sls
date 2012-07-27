mongodb_repo_key:
  cmd.run:
    - name: apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
    - unless: apt-key list | grep -Fq 7F0CEB10

mongodb_repo_src:
  file.managed:
    - name: /etc/apt/sources.list.d/10gen.list
    - source: salt://packages/nosql/10gen.list

mongodb_repo_sync:
  cmd.run:
    - name: apt-get update
    - unless: apt-cache search mongodb-10gen | grep -Fq mongodb-10gen
    - require:
      - cmd: mongodb_repo_key
      - file: mongodb_repo_src

mongodb:
  pkg:
    - installed
    - name: mongodb-10gen
  require:
    - cmd: mongodb_repo_sync

  service:
    - running
