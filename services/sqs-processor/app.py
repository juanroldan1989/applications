from flask import Flask, render_template, jsonify # type: ignore
import boto3 # type: ignore
import os
import requests # type: ignore

app = Flask(__name__)

# Environment variables
QUEUE_URL = os.getenv("SQS_QUEUE_URL")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
REGION_NAME = os.getenv("AWS_REGION")
LOCALSTACK_ENDPOINT = os.getenv("LOCALSTACK_ENDPOINT")

# Conditional initialization of SQS client
if LOCALSTACK_ENDPOINT:
  # Using LocalStack for local development
  print("Using LocalStack for SQS")
  sqs_client = boto3.client("sqs",
                            region_name=REGION_NAME,
                            endpoint_url=LOCALSTACK_ENDPOINT,
                            aws_access_key_id="test",
                            aws_secret_access_key="test",
                            use_ssl=False)
else:
  # Using AWS for production
  print("Using AWS for SQS")
  sqs_client = boto3.client("sqs", region_name=REGION_NAME)

# In-memory store for messages
processed_messages = []
message_counter = 0

def process_message(message_body):
  global message_counter
  processed_message = f"PROCESSED: {message_body}"
  processed_messages.append(processed_message)
  message_counter += 1
  return processed_message

def send_to_slack(processed_message):
  if SLACK_WEBHOOK_URL:
    response = requests.post(
      SLACK_WEBHOOK_URL,
      json={"text": processed_message},
      headers={"Content-Type": "application/json"}
    )
    if response.status_code != 200:
      print(f"Failed to send message to Slack: {response.text}")
    else:
      print("Message sent to Slack successfully")

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/api/poll-sqs')
def poll_sqs():
  """Poll the SQS queue for messages, process them, and return new messages."""
  try:
    response = sqs_client.receive_message(
      QueueUrl=QUEUE_URL,
      MaxNumberOfMessages=10,
      WaitTimeSeconds=0
    )

    messages = response.get("Messages", [])
    if not messages:
      return jsonify({"new_messages": [], "counter": message_counter})

    new_messages = []
    for message in messages:
      body = message["Body"]
      print(f"Received message: {body}")

      # Process message
      processed_message = process_message(body)
      new_messages.append(processed_message)

      # Send processed message to Slack (if enabled)
      send_to_slack(processed_message)

      # Delete message from the queue
      sqs_client.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=message["ReceiptHandle"]
      )
      print("Message deleted from queue")

    return jsonify({"new_messages": new_messages, "counter": message_counter})

  except Exception as e:
    print(f"Error while polling SQS: {str(e)}")
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5005)
