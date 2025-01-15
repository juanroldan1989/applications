import unittest
import json
from app import app

class RandomNameApiTestCase(unittest.TestCase):

  def setUp(self):
    """Set up the test client before each test."""
    self.app = app.test_client()
    self.app.testing = True

  def test_get_name_status_code(self):
    """Test that the /name endpoint returns a 200 status code."""
    response = self.app.get('/name')
    self.assertEqual(response.status_code, 200)

  def test_get_name_content_type(self):
    """Test that the /name endpoint returns JSON content."""
    response = self.app.get('/name')
    self.assertEqual(response.content_type, 'application/json')

  def test_get_name_response_format(self):
    """Test that the response contains a 'name' key."""
    response = self.app.get('/name')
    data = json.loads(response.data)
    self.assertIn('name', data)

  def test_get_name_validity(self):
    """Test that the 'name' in the response is one of the expected names."""
    response = self.app.get('/name')
    data = json.loads(response.data)
    self.assertIn(data['name'], ["Alice", "Bob", "Charlie", "Daisy", "Eve"])

  def test_health_status_code(self):
    """Test that the /health endpoint returns a 200 status code."""
    response = self.app.get('/health')
    self.assertEqual(response.status_code, 200)

  def test_health_content_type(self):
    """Test that the /health endpoint returns JSON content."""
    response = self.app.get('/health')
    self.assertEqual(response.content_type, 'application/json')

  def test_health_response_format(self):
    """Test that the response contains a 'status' key with value 'healthy'."""
    response = self.app.get('/health')
    data = json.loads(response.data)
    self.assertIn('status', data)
    self.assertEqual(data['status'], 'healthy')

if __name__ == '__main__':
  unittest.main()
