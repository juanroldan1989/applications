import unittest
import json
from app import app

class GreetingApiTestCase(unittest.TestCase):

  def setUp(self):
    """Set up the test client before each test."""
    self.app = app.test_client()
    self.app.testing = True

  def test_get_greeting_status_code(self):
    """Test that the /greeting endpoint returns a 200 status code."""
    response = self.app.get('/greeting')
    self.assertEqual(response.status_code, 200)

  def test_get_greeting_content_type(self):
    """Test that the /greeting endpoint returns JSON content."""
    response = self.app.get('/greeting')
    self.assertEqual(response.content_type, 'application/json')

  def test_get_greeting_response_format(self):
    """Test that the response contains a 'greeting' key."""
    response = self.app.get('/greeting')
    data = json.loads(response.data)
    self.assertIn('greeting', data)

  def test_get_greeting_validity(self):
    """Test that the 'greeting' in the response is one of the expected greetings."""
    response = self.app.get('/greeting')
    data = json.loads(response.data)
    self.assertIn(data['greeting'], ["Hello", "Hi", "Greetings", "Salutations", "Hey"])

  def test_health_status_code(self):
    """Test that the /health endpoint returns a 200 status code."""
    response = self.app.get('/health')
    self.assertEqual(response.status_code, 200)

  def test_health_content_type(self):
    """Test that the /health endpoint returns JSON content."""
    response = self.app.get('/health')
    self.assertEqual(response.content_type, 'application/json')

  def test_health_response(self):
    """Test that the /health endpoint returns a status of 'healthy'."""
    response = self.app.get('/health')
    data = json.loads(response.data)
    self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
  unittest.main()
