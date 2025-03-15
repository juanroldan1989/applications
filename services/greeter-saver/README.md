# Greeter Saver App

- This is a Flask-based microservice that communicates with two other services, **Name API** and **Greeting API**, to generate a personalized greeting message.

- Each greeting message is stored in a database (e.g.: full message and timestamp).

## Features

- Fetches a random name from the **Name Service**.
- Fetches a random greeting from the **Greeting Service**.
- Combines the name and greeting to return a friendly message.
- **Stores message in database.**
- Health check endpoint for monitoring the API status.
- Includes logging for better error tracking and debugging.
- Lightweight, containerized, and easy to deploy.

## Endpoints

### `GET /greet`

1. Fetches a greeting and name from the external services and returns a combined message.

- Response:

```bash
{
  "message": "Hello, Alice!"
}
```

2. Stores message in database:

```bash
docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS                    PORTS                    NAMES
4aff547e83a5   applications-greeter-saver   "flask run --host=0.…"   18 seconds ago   Up 12 seconds             0.0.0.0:5008->5008/tcp   greeter-saver
2612ef2bca14   postgres:13-alpine           "docker-entrypoint.s…"   18 seconds ago   Up 18 seconds (healthy)   0.0.0.0:5432->5432/tcp   database
3995a0ccba5d   applications-greeting        "flask run --host=0.…"   18 seconds ago   Up 18 seconds (healthy)   0.0.0.0:5002->5002/tcp   greeting
1656d2723bb1   applications-name            "flask run --host=0.…"   18 seconds ago   Up 18 seconds (healthy)   0.0.0.0:5001->5001/tcp   name
```

```bash
docker exec -it database psql -U user -d mydatabase
```

```bash
mydatabase=# SELECT * from "greetings";
 id |       message       |         created_at
----+---------------------+----------------------------
  1 | Hey, Alice!         | 2025-03-15 10:56:19.238592
  2 | Hello, Daisy!       | 2025-03-15 10:56:20.297562
  3 | Hello, Eve!         | 2025-03-15 10:56:20.724796
  4 | Hey, Charlie!       | 2025-03-15 10:56:20.973966
  5 | Salutations, Alice! | 2025-03-15 10:56:21.197505
  6 | Hi, Charlie!        | 2025-03-15 10:56:21.394144
  7 | Hi, Alice!          | 2025-03-15 10:56:21.587393
  8 | Salutations, Daisy! | 2025-03-15 10:56:21.785991
  9 | Hi, Charlie!        | 2025-03-15 10:56:25.532674
 10 | Greetings, Bob!     | 2025-03-15 10:56:25.728187
 11 | Hi, Bob!            | 2025-03-15 10:56:25.96401
 12 | Hey, Charlie!       | 2025-03-15 10:56:26.135074
(12 rows)
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
http://localhost:5008
```

## Environment Variables

- `NAME_SERVICE_URL`: URL for the name generator service. Default is http://name:5001/name.
- `GREETING_SERVICE_URL`: URL for the greeting service. Default is http://greeting:5002/greeting.
- `DATABASE_URL`: URL for the database endpoint to which save messages. Messages stored only when value is provided.

Example:

```bash
export NAME_SERVICE_URL="http://localhost:5001/name"
export GREETING_SERVICE_URL="http://localhost:5002/greeting"
export DATABASE_URL="postgresql://username@host:5432/mydatabase"
```

## Deployment

### Docker

- Build and run the applications:

```bash
cd applications

docker-compose up name greeting greeter-saver database --build
```

- Access App at http://localhost:5008

### Docker Compose clean up

- Quickly clean up everything (including `data` volumes):

```bash
docker-compose down -v
[+] Running 6/6

✔ Container greeter-saver       Removed
✔ Container database            Removed
✔ Container greeting            Removed
✔ Container name                Removed
✔ Volume applications_pgdata    Removed
✔ Network applications_backend  Removed
```

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
