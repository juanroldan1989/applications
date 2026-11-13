import unittest
from unittest.mock import patch
import json
import requests
from app import app

class GreeterServiceTestCase(unittest.TestCase):
  def setUp(self):
    """Set up the test client before each test."""
    self.app = app.test_client()
    self.app.testing = True

  @patch('requests.get')
  def test_greet_with_mocked_services(self, mock_get):
    """Test the /greet endpoint with mocked external services."""
    mock_get.side_effect = [
      unittest.mock.Mock(status_code=200, json=lambda: {'name': 'Alice'}),  # Mock for name service
      unittest.mock.Mock(status_code=200, json=lambda: {'greeting': 'Hello'})  # Mock for greeting service
    ]

    response = self.app.get('/greet')
    data = json.loads(response.data)

    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['message'], 'Hello, Alice!')

  @patch('requests.get')
  def test_greet_status_code(self, mock_get):
    """Test that the /greet endpoint returns a 200 status code."""
    mock_get.side_effect = [
      unittest.mock.Mock(json=lambda: {'name': 'Alice'}),
      unittest.mock.Mock(json=lambda: {'greeting': 'Hello'})
    ]
    response = self.app.get('/greet')
    self.assertEqual(response.status_code, 200)

  @patch('requests.get')
  def test_greet_content_type(self, mock_get):
    """Test that the /greet endpoint returns JSON content."""
    mock_get.side_effect = [
      unittest.mock.Mock(json=lambda: {'name': 'Alice'}),
      unittest.mock.Mock(json=lambda: {'greeting': 'Hello'})
    ]
    response = self.app.get('/greet')
    self.assertEqual(response.content_type, 'application/json')

  @patch('requests.get')
  def test_greet_response_format(self, mock_get):
    """Test that the /greet endpoint contains a 'message' key."""
    mock_get.side_effect = [
      unittest.mock.Mock(json=lambda: {'name': 'Alice'}),
      unittest.mock.Mock(json=lambda: {'greeting': 'Hello'})
    ]
    response = self.app.get('/greet')
    data = json.loads(response.data)
    self.assertIn('message', data)

  @patch('requests.get')
  def test_greet_returns_503_when_service_unreachable(self, mock_get):
    """Test that the /greet endpoint returns 503 when a dependency fails."""
    mock_get.side_effect = requests.ConnectionError('boom')
    response = self.app.get('/greet')
    self.assertEqual(response.status_code, 503)

  def test_health_status_code(self):
    """Test that the /health endpoint returns a 200 status code."""
    response = self.app.get('/health')
    self.assertEqual(response.status_code, 200)

  def test_health_response_format(self):
    """Test that the /health endpoint contains a 'status' key."""
    response = self.app.get('/health')
    data = json.loads(response.data)
    self.assertIn('status', data)

if __name__ == '__main__':
  unittest.main()
