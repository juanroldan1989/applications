# Fareweller App

The Fareweller App is a Flask-based microservice that interacts with two other services to generate personalized farewell messages.

It fetches a random name and a random farewell phrase from external services, combines them, and returns a farewell message.

## Features

- Fetches a random name from `Name App` service.
- Fetches a random farewell phrase from `Farewell App` service.
- Combines the name and phrase into a personalized farewell message.
- Health check endpoint for monitoring the API status.
- Includes logging for better error tracking and debugging.
- Lightweight, containerized, and easy to deploy.

## Endpoints

### `GET /`

Returns a personalized farewell message.

- Example Response:

```bash
{
  "message": "Goodbye, Alice!"
}
```

## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install flask
```

3. Run the application:

```bash
python app.py
```

4. Access the API: Open your browser or a tool like curl or Postman and navigate to:

```bash
http://localhost:5003
```

## Environment Variables

- `NAME_SERVICE_URL`: URL for the name generator service. Default is http://name:5001/name.
- `FAREWELL_SERVICE_URL`: URL for the farewell phrase service. Default is http://farewell:5004/phrase.

Example:

```bash
export NAME_SERVICE_URL="http://localhost:5001/name"
export FAREWELL_SERVICE_URL="http://localhost:5004/phrase"
```

## Deployment

### Docker

- Build and run the Docker container:

```bash
docker build -t name-api .
docker run -d -p 5001:5001 name-api

docker build -t farewell-api .
docker run -d -p 5004:5004 farewell-api

docker build -t fareweller-api .
docker run -d -p 5003:5003 fareweller-api
```

- Access the API at http://localhost:5003

### Using ECS and EKS

This Flask app is designed to be easily deployable in AWS ECS and EKS clusters.

Here's an overview of how to deploy it:

- ECS Deployment:

1. Create a Docker image of the app and push it to a container registry like Docker Hub or Amazon Elastic Container Registry (ECR).
2. Use Terraform or AWS CloudFormation to define the ECS task and service.
3. Deploy the app as an ECS service behind an Application Load Balancer (ALB) to ensure high availability.

- EKS Deployment:

1. Build and push the Docker image to a container registry.
2. Define a Kubernetes deployment and service YAML file to deploy the app in the EKS cluster.
3. Use kubectl to apply the deployment and service definitions.
4. Expose the service using a LoadBalancer service type or an Ingress resource.

## Unit Tests

Unit tests are provided to ensure the correctness of the API. The tests cover the following:

- Status code verification.
- JSON content type verification.
- Proper handling of external service failures.
- Ensuring the response contains a valid farewell phrase.

### How to Run Unit Tests

Ensure you have Python and the required dependencies installed:

```bash
pip install -r requirements.txt
```

Run the unit tests:

```bash
python -m unittest test_app.py
```

### Test Coverage

The following tests are included:

- `test_farewell_status_code`: Verifies that the / endpoint returns a 200 status code.
- `test_farewell_content_type`: Ensures that the content type of the response is application/json.
- `test_farewell_response_format`: Ensures that the response contains a key named message.
- `test_health_status_code`: Verifies that the /health endpoint returns a 200 status code.
- `test_health_response_format`: Ensures that the /health endpoint returns the correct status in JSON format.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
