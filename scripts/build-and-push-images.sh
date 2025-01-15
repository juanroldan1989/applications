#!/bin/bash

for app in farewell greeting greeter fareweller name sqs-processor; do
  echo "Building Docker image for $app..."
  cd services/$app
  docker build -t juanroldan1989/$app .
  docker push juanroldan1989/$app
  cd ..
done
