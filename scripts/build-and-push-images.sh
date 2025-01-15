#!/bin/bash

# Change to the services directory
cd ../services

# Build and push images for all services
for app in farewell greeting greeter fareweller name sqs-processor; do
  echo "Building Docker image for $app..."
  cd $app
  docker build -t juanroldan1989/$app .
  docker push juanroldan1989/$app
  cd ..
done
