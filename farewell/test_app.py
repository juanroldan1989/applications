import unittest
import json
from app import app

class FarewellApiTestCase(unittest.TestCase):

  def setUp(self):
    """Set up the test client before each test."""
    self.app = app.test_client()
    self.app.testing = True

  def test_get_phrase_status_code(self):
    """Test that the /phrase endpoint returns a 200 status code."""
    response = self.app.get('/phrase')
    self.assertEqual(response.status_code, 200)

  def test_get_phrase_content_type(self):
    """Test that the /phrase endpoint returns JSON content."""
    response = self.app.get('/phrase')
    self.assertEqual(response.content_type, 'application/json')

  def test_get_phrase_response_format(self):
    """Test that the response contains a 'phrase' key."""
    response = self.app.get('/phrase')
    data = json.loads(response.data)
    self.assertIn('phrase', data)

  def test_get_phrase_validity(self):
    """Test that the 'phrase' in the response is one of the expected farewells."""
    response = self.app.get('/phrase')
    data = json.loads(response.data)
    self.assertIn(data['phrase'], [
        "See ya later", "Peace out", "Adios", "Ciao",
        "Sayonara", "Hasta la vista", "Auf Wiedersehen",
        "Arrivederci", "Chow", "Ta-ta", "Cheerio"
    ])

if __name__ == '__main__':
  unittest.main()
