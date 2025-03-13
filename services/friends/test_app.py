import unittest
from unittest.mock import patch
import json
from app import app
import os

class FriendsServiceTestCase(unittest.TestCase):
  def setUp(self):
    """Set up the test client before each test."""
    self.app = app.test_client()
    self.app.testing = True

  @patch('requests.get')
  def test_home_greeting_with_mocked_services(self, mock_get):
    """Test the home endpoint with mocked external services."""
    # Set up the two mocks: one for the name service and one for the greeting service.
    mock_get.side_effect = [
      unittest.mock.Mock(status_code=200, json=lambda: {'name': 'Alice'}),
      unittest.mock.Mock(status_code=200, json=lambda: {'greeting': 'Hello'})
    ]

    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)
    html = response.get_data(as_text=True)

    # Check that the greeting message is rendered in the HTML.
    self.assertIn("Hello, Alice!", html)

  def test_health_status_code(self):
    """Test that the /health endpoint returns a 200 status code."""
    response = self.app.get('/health')
    self.assertEqual(response.status_code, 200)

  def test_health_response_format(self):
    """Test that the /health endpoint contains a 'status' key."""
    response = self.app.get('/health')
    data = json.loads(response.data)
    self.assertIn('status', data)

  def test_index_returns_html_and_includes_friend_image(self):
    """Test that the index route returns HTML content including the friend image reference."""
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)
    # Verify that the response content type is HTML
    self.assertIn('text/html', response.content_type)
    # Check that the friend image filename (set via env var) is included in the rendered template.
    friend = os.getenv("FRIEND", "phoebe").lower()
    friend_image = f"{friend}.png"
    self.assertIn(friend_image, response.get_data(as_text=True))

if __name__ == '__main__':
  unittest.main()
