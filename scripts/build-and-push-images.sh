#!/bin/bash

# Set the Docker image tag to the first input parameter, or default to "latest"
TAG=${1:-latest}

# example: ./scripts/build-and-push-images.sh 0.0.1

# Change to the services directory
cd ../services

# Build and push images for all services
for app in name farewell greeting greeter greeter-saver fareweller sqs-processor; do
  echo "Building Docker image for $app with tag $TAG..."
  cd $app

  # Docker images built with multi-platform support (Linux/amd64 and Linux/arm64)
  docker buildx build --platform linux/amd64,linux/arm64 -t juanroldan1989/$app:$TAG .
  # Useful for development on Apple M1 or other ARM-based systems
  # Useful for deployments on ARM-based systems like Raspberry Pi
  # Useful for deployments on EKS Nodes with x86_64 (amd64) architecture

  # Push the tagged image to the repository
  docker push juanroldan1989/$app:$TAG

  cd ..
done

# Build and push images for "friends" service using each "characther" as TAG
cd friends
for friend in chandler joey monica phoebe rachel ross; do
  echo "Building Docker image for "friends" with tag $friend..."

  docker buildx build --platform linux/amd64,linux/arm64 --build-arg FRIEND=$friend -t juanroldan1989/friends:$friend .
  docker push juanroldan1989/friends:$friend
done
