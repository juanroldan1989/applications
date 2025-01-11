import unittest
import json
from unittest.mock import patch
from app import app

class FarewellerAppTestCase(unittest.TestCase):

  def setUp(self):
    """Set up the test client before each test."""
    self.app = app.test_client()
    self.app.testing = True

  @patch("app.requests.get")
  def test_farewell_status_code(self, mock_get):
    """Test that the / endpoint returns a 200 status code."""
    mock_get.side_effect = [
        unittest.mock.Mock(json=lambda: {"name": "Alice"}),
        unittest.mock.Mock(json=lambda: {"phrase": "Goodbye"})
    ]
    response = self.app.get("/")
    self.assertEqual(response.status_code, 200)

  @patch("app.requests.get")
  def test_farewell_content_type(self, mock_get):
    """Test that the / endpoint returns JSON content."""
    mock_get.side_effect = [
        unittest.mock.Mock(json=lambda: {"name": "Alice"}),
        unittest.mock.Mock(json=lambda: {"phrase": "Goodbye"})
    ]
    response = self.app.get("/")
    self.assertEqual(response.content_type, "application/json")

  @patch("app.requests.get")
  def test_farewell_response_format(self, mock_get):
    """Test that the response contains a 'message' key."""
    mock_get.side_effect = [
        unittest.mock.Mock(json=lambda: {"name": "Alice"}),
        unittest.mock.Mock(json=lambda: {"phrase": "Goodbye"})
    ]
    response = self.app.get("/")
    data = json.loads(response.data)
    self.assertIn("message", data)

  def test_health_status_code(self):
    """Test that the /health endpoint returns a 200 status code."""
    response = self.app.get("/health")
    self.assertEqual(response.status_code, 200)

  def test_health_response_format(self):
    """Test that the /health endpoint returns the correct JSON format."""
    response = self.app.get("/health")
    data = json.loads(response.data)
    self.assertEqual(data, {"status": "healthy"})

if __name__ == "__main__":
  unittest.main()
