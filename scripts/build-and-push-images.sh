#!/bin/bash

for app in farewell greeting greeter fareweller name sqs-processor; do
  echo "Building Docker image for $app..."
  cd $app
  docker build -t <docker-hub-username>/$app .
  docker push <docker-hub-username>/$app
  cd ..
done
