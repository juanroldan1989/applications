#!/bin/bash

# Change to the services directory
cd ../services

# Build and push images for all services
for app in farewell greeting greeter fareweller name sqs-processor; do
  echo "Building Docker image for $app..."
  cd $app

  # Docker images built with multi-platform support (Linux/amd64 and Linux/arm64)
  docker buildx build --platform linux/amd64,linux/arm64 -t juanroldan1989/$app .
  # Useful for development on Apple M1 or other ARM-based systems
  # Useful for deployments on ARM-based systems like Raspberry Pi
  # Useful for deployments on EKS Nodes with x86_64 (amd64) architecture

  docker push juanroldan1989/$app
  cd ..
done
