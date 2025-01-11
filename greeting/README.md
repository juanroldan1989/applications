# Greeting API

This is a simple Flask-based API that returns a random greeting message from a predefined list.

## Features

- Provides a random greeting via a simple GET request.
- Lightweight and easy to deploy.
- Includes health check for monitoring purposes.

## Endpoints

### `GET /greeting`

Returns a random greeting in JSON format.

- Example Response:

```bash
{
  "greeting": "Hello"
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
http://localhost:5002/greeting
```

## Deployment

### Docker

- Build and run the Docker container:

```bash
docker build -t greeting-api .
docker run -d -p 5002:5002 greeting-api
```

- Access the API at http://localhost:5002/greeting.

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
- Ensuring the response contains a valid greeting.

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

- `test_get_greeting_status_code`: Verifies that the /greeting endpoint returns a 200 status code.
- `test_get_greeting_content_type`: Ensures the content type of the response is application/json.
- `test_get_greeting_response_format`: Checks that the response contains a key named greeting.
- `test_get_greeting_validity`: Ensures the returned greeting is from the predefined list of greetings.
- `test_health_status_code`: Verifies that the /health endpoint returns a 200 status code.
- `test_health_content_type`: Ensures the content type of the /health endpoint response is application/json.
- `test_health_response`: Checks that the /health endpoint returns a status of healthy.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
