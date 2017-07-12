#!/bin/bash

docker build -t basicinventory /vagrant/basicinventory
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker run -d -p 80:8000 -v /vagrant/basicinventory/db.sqlite3:/app/db.sqlite3 --name=app basicinventory
