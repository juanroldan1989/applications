#!/bin/sh

# Remove all images
docker rmi $(docker images -q) -f

# Remove all containers
docker rm $(docker ps -a -q) -f

# Remove all volumes
docker volume rm $(docker volume ls -q) -f
