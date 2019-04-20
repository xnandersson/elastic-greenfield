Install
-------

.. code:: bash

  $ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  $ echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
  $ sudo apt-get update
  $ sudo apt install filebeat -y

Setup
-----

.. code:: bash

  $ docker-compose up
  $ cd src && python generate-filebeat-conf.py && sudo cp filebeat.yml /etc/filebeat/filebeat.yml
  $ sudo systemctl restart filebeat

