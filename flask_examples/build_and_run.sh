#!/bin/bash

docker build -t hiera_backend_app /vagrant/flask_examples
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker run -d -p 80:5000 --name=app hiera_backend_app
