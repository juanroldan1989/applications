#!/bin/sh

# Remove all images
docker image ls | grep applications | awk '{print $3}' | xargs docker image rm -f

# Remove all containers
docker rm $(docker ps -a -q) -f

# Remove all volumes
docker volume rm $(docker volume ls -q) -f
