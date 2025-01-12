from flask import Flask, jsonify
import requests
import logging
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# External service URLs (configurable via environment variables)
NAME_SERVICE_URL = os.getenv("NAME_SERVICE_URL", "http://name:5001/name")
GREETING_SERVICE_URL = os.getenv("GREETING_SERVICE_URL", "http://greeting:5002/greeting")

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
  try:
    # Fetch name and greeting with timeouts
    name_response = requests.get(NAME_SERVICE_URL, timeout=5)
    greeting_response = requests.get(GREETING_SERVICE_URL, timeout=5)

    # Raise exceptions for HTTP errors
    name_response.raise_for_status()
    greeting_response.raise_for_status()

    # Parse JSON responses
    name = name_response.json().get("name")
    greeting = greeting_response.json().get("greeting")

    return jsonify(message=f"{greeting}, {name}!")

  except requests.RequestException as e:
    logger.error(f"Failed to fetch data from external services: {str(e)}")
    return jsonify(error=f"Failed to fetch data from external services: {str(e)}"), 503
  except Exception as e:
    logger.error(f"An unexpected error occurred: {str(e)}")
    return jsonify(error=f"An unexpected error occurred: {str(e)}"), 500

@app.route('/health', methods=['GET'])
def health():
  return jsonify(status='healthy')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
