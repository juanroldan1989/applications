import unittest
from unittest.mock import patch, MagicMock
from app import app, process_message, send_to_slack

class FlaskAppTestCase(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True

  @patch("app.sqs_client.receive_message")
  @patch("app.sqs_client.delete_message")
  @patch("app.send_to_slack")
  def test_poll_sqs_success(self, mock_send_to_slack, mock_delete_message, mock_receive_message):
    # Mock response from SQS
    mock_receive_message.return_value = {
      "Messages": [
        {"Body": "Test message", "ReceiptHandle": "abc123"}
      ]
    }
    response = self.app.get('/api/poll-sqs')
    self.assertEqual(response.status_code, 200)
    self.assertIn("new_messages", response.json)
    self.assertEqual(response.json["new_messages"], ["PROCESSED: Test message"])
    self.assertEqual(response.json["counter"], 1)

    # Ensure message was processed and deleted
    mock_delete_message.assert_called_once_with(
      QueueUrl="test_queue_url", ReceiptHandle="abc123"
    )
    mock_send_to_slack.assert_called_once_with("PROCESSED: Test message")

  @patch("app.sqs_client.receive_message")
  def test_poll_sqs_no_messages(self, mock_receive_message):
    # Mock empty response from SQS
    mock_receive_message.return_value = {"Messages": []}
    response = self.app.get('/api/poll-sqs')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json["new_messages"], [])
    self.assertEqual(response.json["counter"], 0)

  @patch("app.sqs_client.receive_message")
  def test_poll_sqs_error(self, mock_receive_message):
    # Mock an exception when polling SQS
    mock_receive_message.side_effect = Exception("SQS error")
    response = self.app.get('/api/poll-sqs')
    self.assertEqual(response.status_code, 500)
    self.assertIn("error", response.json)
    self.assertEqual(response.json["error"], "SQS error")

  @patch("app.requests.post")
  def test_send_to_slack_success(self, mock_post):
    mock_post.return_value.status_code = 200
    send_to_slack("Test Slack message")
    mock_post.assert_called_once_with(
      "test_webhook_url",
      json={"text": "Test Slack message"},
      headers={"Content-Type": "application/json"}
    )

  @patch("app.requests.post")
  def test_send_to_slack_failure(self, mock_post):
    mock_post.return_value.status_code = 500
    mock_post.return_value.text = "Slack error"
    send_to_slack("Test Slack message")
    mock_post.assert_called_once()
    print("Ensure error message logged when Slack fails.")

  def test_process_message(self):
    result = process_message("Hello World")
    self.assertEqual(result, "PROCESSED: Hello World")
