# SQS Message Processor Flask App

## Features

- Polls an SQS queue for messages every 5 seconds.
- Processes messages by adding the `PROCESSED:` prefix.
- Optionally sends the processed messages to a Slack channel if the `SLACK_WEBHOOK_URL` is provided.
- Displays the processed messages and the number of messages processed on the home page.
- The application includes a top navigation bar, a footer, and a responsive two-column layout using Tailwind CSS.

## Environment Variables

Ensure the following environment variables are set:

- `SQS_QUEUE_URL`: The URL of your SQS queue.
- `SLACK_WEBHOOK_URL` (Optional): The Slack webhook URL to send processed messages (if not provided, messages won't be sent to Slack).
- `AWS_REGION` (Optional, default: `us-east-1`): The AWS region where the SQS queue is located.
- `LOCALSTACK_ENDPOINT` (Optional): The LocalStack endpoint to use for local development (default: not set). When provided, the app will use LocalStack for SQS interactions.

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Set the environment variables. For example, on Linux/Mac:

```bash
export SQS_QUEUE_URL="your_sqs_queue_url"
export SLACK_WEBHOOK_URL="your_slack_webhook_url"  # Optional
export AWS_REGION="us-east-1"  # Optional
export LOCALSTACK_ENDPOINT="https://localhost.localstack.cloud:4566"  # Optional (for LocalStack)
```

3. Run the application:

```bash
python app.py
```

The Flask app will be available at `http://127.0.0.1:5005/`

## Diagram

```bash
                          +----------------------------+
                          |    SQS Message Processor   |
                          |         Flask App          |
                          +----------------------------+
                                       |
        +------------------------------+-------------------------------+
        |                                                              |
+----------------------+                                   +------------------------+
|    SQS Queue         |                                   |  Slack Channel (Optional)|
|----------------------|                                   |--------------------------|
| - Poll every 5 sec   |                                   | - Send processed messages |
| - Receive messages   |                                   |   if webhook is provided  |
+----------------------+                                   +--------------------------+
        |
        | Process Messages (Add "PROCESSED:" Prefix)
        v
+-----------------------+
|  Flask Application    |
|-----------------------|
| - app.py              |
| - Poll SQS queue      |
| - Send to Slack (Opt) |
| - Serve Web Interface |
+-----------------------+
        |
        v
+-----------------------+
| Web Interface         |
|-----------------------|
| - Home Page           |
|   - List messages     |
|   - Show message count|
+-----------------------+
        |
        v
+---------------------------+
| LocalStack Support (Opt.) |
|---------------------------|
| - Use for local dev       |
| - Connect to LocalStack   |
+---------------------------+
```

## How It Works

1. **SQS Polling:** The app uses a background polling mechanism (frontend javascript) to check the SQS queue every 5 seconds for new messages, using either AWS or LocalStack depending on the configuration.

2. **Message Processing:** Each message is processed by adding the PROCESSED: prefix.

3. **Slack Integration:** If the SLACK_WEBHOOK_URL is set, the processed messages are sent to Slack.

4. **Web Interface:** The home page displays:

- A list of processed messages.
- A counter showing how many messages have been processed.

5. **LocalStack Support:** If the LOCALSTACK_ENDPOINT environment variable is set, the app will connect to LocalStack for local SQS interactions, instead of using AWS. This is useful for local development.

## API Endpoints

- `/`: The home page that displays the processed messages and message count.
- `/api/messages`: Returns the list of processed messages in JSON format.
- `/api/counter`: Returns the current message count in JSON format.

## Application Structure

- `app.py`: The main Flask application that handles SQS polling and serves the web interface.

- `templates/index.html`: The HTML template for the home page, which displays the processed messages and the counter and contains the JS script that polls messages from the SQS queue.

## Deployment

1. SQS Processor App containerised via Dockerfile.
2. SQS Processor App provisioned within ECS Task:

- ENV Variables defined for ECS Task:

a. `SQS_QUEUE_URL`: dependency.sqs-queue-a.outputs.queue_url
b. `LOCALSTACK_ENDPOINT`: `https://localhost.localstack.cloud:4566`

3. Deployment into LocalStack within ECS Service (with Load Balancer)

4. Access SQS Processor App via ALB DNS_NAME:

```bash
http://alb-sqs-processor-mirror.elb.localhost.localstack.cloud:5005/
```

5. Push Message into SQS Queue:

```bash
aws sqs send-message \
  --endpoint-url http://localhost:4566 \
  --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/queue-a \
  --message-body "Hello from LocalStack" --profile default
```

6. Message displayed within LocalStack cloud interface for SQS Queue A:

<img width="1367" alt="Screenshot 2025-01-06 at 15 55 28" src="https://github.com/user-attachments/assets/634e8908-5237-4f7d-911a-13e12f13bd80" />

7. Message pulled and processed by SQS Processor App:

<img width="799" alt="Screenshot 2025-01-06 at 15 48 11" src="https://github.com/user-attachments/assets/329002c3-79e2-4cd3-8d3b-023151a44099" />

8. Message removed from SQS Queue afterwards by App.

## Unit Tests

Unit tests are provided to ensure the correctness of the API. The tests cover the following:

- Status code verification.
- JSON content type verification.
- Ensuring the response contains a valid farewell phrase.

### How to Run Unit Tests

Ensure you have Python and the required dependencies installed:

```bash
pip install flask
```

Run the unit tests:

```bash
python -m unittest test_app.py
```

### Test Coverage

The following tests are included:

1. `test_poll_sqs_success`:

- Mocks SQS to return a single message.
- Verifies the correct processing of the message and deletion from the queue.
- Checks that the processed message is sent to Slack.

2. `test_poll_sqs_no_messages`:

- Mocks SQS with an empty response.
- Verifies that the endpoint correctly handles the case where no messages are available.

3. `test_poll_sqs_error`:

- Simulates an exception during SQS polling and ensures that the error is returned with a 500 status code.

4. `test_send_to_slack_success`:

- Mocks a successful Slack post request and verifies that it is called with the correct payload.

5. `test_send_to_slack_failure`:

- Simulates a failure when posting to Slack and ensures that the appropriate error message is logged.

6. `test_process_message`:

- Verifies that the process_message function works as expected by appending "PROCESSED:" to the message.

## Tailwind CSS

The app uses Tailwind CSS for styling. The page is divided into two sections:

- Left Section: Displays the processed messages.
- Right Section: Displays the message count.

- Both sections are centered within their respective areas.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
