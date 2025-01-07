# Applications

A collection of simple yet powerful microservices designed for cloud-native applications.

This repository serves as a portfolio of reusable Flask applications, each one designed to be modular, lightweight

and easily integrable with containerized environments like **AWS ECS** and **AWS EKS**.

# Contents

This repository contains the following Flask applications:

1. **Farewell API**  
   Returns a random farewell phrase.

2. **Fareweller API**  
   Returns a farewell message built based on Farewell and Name APIs.

3. **Greeter API**  
   Returns a greeting message built based on Greeting and Name APIs.

4. **Greeting API**  
   Provides greeting phrases.

5. **Name API**  
   Supplies random names.

6. **SQS Processor**  
   Processes SQS messages and displays states within a landing page.

# Use Cases

These applications were created as modular services that can be integrated into larger cloud-native projects.

The primary use cases include:

- **Portfolio Projects**: Demonstrating cloud-native development with Flask, Docker, ECS, EKS, Terraform and Terragrunt.
- **Reusable Modules**: Serving as building blocks for larger microservice architectures.
- **Learning & Experimentation**: Providing a playground for experimenting with cloud technologies, CI/CD pipelines and container orchestration.

# How to Build and Push Docker Images

## Build and Push Manually (Bash Script)

You can build and push all Docker images manually using the following bash script:

```bash
#!/bin/bash

for app in fareweller farewell greeter greeting name sqs-processor; do
  echo "Building Docker image for $app..."
  cd $app
  docker build -t <docker-hub-username>/$app .
  docker push <docker-hub-username>/$app
  cd ..
done
```

## Build and Push Automatically (GitHub Actions)

This repository also includes a GitHub Actions workflow (`.github/workflows/docker-build-and-push.yml`)

that automates the process of building and pushing Docker images to Docker Hub whenever changes are pushed to the repository.

The workflow is triggered on changes to any application directory and performs the following steps:

1. Checks out the code.
2. Sets up Docker.
3. Builds Docker images.
4. Pushes the images to Docker Hub.

# Adding Applications

To add a new Flask application:

1. Create a new folder with the application name.
2. Include the following files:

- `Dockerfile`: Defines how the application will be containerized.
- `app.py`: The main Flask application logic.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation for the application.

3. Update the bash script and GitHub Actions workflow if needed.

# Future Plans

Extend the portfolio with more Flask services for additional use cases.

# License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
