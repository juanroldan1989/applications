# Greeter App

This is a Flask-based microservice that communicates with two other services,

**Name API** and **Greeting API**,

to generate a personalized greeting message.

## Features

- Fetches a random name from the **Name Service**.
- Fetches a random greeting from the **Greeting Service**.
- Combines the name and greeting to return a friendly message.
- Health check endpoint for monitoring the API status.
- Includes logging for better error tracking and debugging.
- Lightweight, containerized, and easy to deploy.

## Endpoints

### `GET /greet`

Fetches a greeting and name from the external services and returns a combined message.

- Response:

```bash
{
  "message": "Hello, Alice!"
}
```

### `GET /health`

Returns the health status of the service.

- Example Response:

```bash
{
  "status": "healthy"
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

4. Access the API:

Open your browser or a tool like curl or Postman and navigate to:

```bash
http://localhost:5000
```

## Environment Variables

- `NAME_SERVICE_URL`: URL for the name generator service. Default is http://name:5001/name.
- `GREETING_SERVICE_URL`: URL for the greeting service. Default is http://greeting:5002/greeting.

Example:

```bash
export NAME_SERVICE_URL="http://localhost:5001/name"
export GREETING_SERVICE_URL="http://localhost:5002/greeting"
```

## Deployment

### Docker

- Build and run the Docker container:

```bash
docker build -t name-api .
docker run -d -p 5001:5001 name-api

docker build -t greeting-api .
docker run -d -p 5002:5002 greeting-api

docker build -t greeter-api .
docker run -d -p 5000:5000 greeter-api
```

- Access the API at http://localhost:5000

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

- `test_greet_status_code`: Verifies that the `/greet` endpoint returns a 200 status code.
- `test_greet_content_type`: Ensures the response has a content type of `application/json`.
- `test_greet_response_format`: Verifies that the response contains a `message` key.
- `test_health_status_code`: Verifies that the `/health` endpoint returns a `200` status code.
- `test_health_response_format`: Ensures that the `/health` endpoint returns the correct status in JSON format.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
