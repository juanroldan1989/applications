import unittest
from unittest.mock import patch
import json
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

  def test_greet_status_code(self):
    """Test that the /greet endpoint returns a 200 status code."""
    response = self.app.get('/greet')
    self.assertEqual(response.status_code, 200)

  def test_greet_content_type(self):
    """Test that the /greet endpoint returns JSON content."""
    response = self.app.get('/greet')
    self.assertEqual(response.content_type, 'application/json')

  def test_greet_response_format(self):
    """Test that the /greet endpoint contains a 'message' key."""
    response = self.app.get('/greet')
    data = json.loads(response.data)
    self.assertIn('message', data)

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
