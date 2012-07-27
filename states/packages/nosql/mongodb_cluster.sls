include:
  - packages.nosql.mongodb

mongodb_key:
  file.managed:
    - name: /etc/mongodb.key
    - source: salt://packages/nosql/mongodb/mongodb.key
    - mode: 600
    - user: mongodb
    - group: mongodb
    - require:
      - file: mongodb_conf
  
mongodb_conf:
  file.append:
  - name: /etc/mongodb.conf
  - text:
    - replSet = WiLog
    - rest = true
    - auth = true
    - keyFile = /etc/mongodb.key

extend:
  mongodb:
    service:
      - watch:
        - file: /etc/mongodb.key