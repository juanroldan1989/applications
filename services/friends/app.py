from flask import Flask, jsonify, render_template, url_for
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

@app.route('/', methods=['GET'])
def home():
  # Validate friend from environment variable
  allowed_friends = ["ross", "rachel", "chandler", "joey", "monica", "phoebe"]
  friend = os.getenv("FRIEND")
  if friend not in allowed_friends:
    friend = "chandler"
  friend_image = f"{friend}.png"

  # Fetch name and greeting with timeouts and build the message
  try:
    name_response = requests.get(NAME_SERVICE_URL, timeout=5)
    greeting_response = requests.get(GREETING_SERVICE_URL, timeout=5)
    name_response.raise_for_status()
    greeting_response.raise_for_status()

    name = name_response.json().get("name")
    greeting = greeting_response.json().get("greeting")
    message = f"{greeting}, {name}!"
  except requests.RequestException as e:
    logger.error(f"Failed to fetch data from external services: {str(e)}")
    message = "Error fetching greeting."
  except Exception as e:
    logger.error(f"An unexpected error occurred: {str(e)}")
    message = "Unexpected error occurred."

  return render_template("index.html", friend_image=friend_image, message=message)

@app.route('/health', methods=['GET'])
def health():
  return jsonify(status='healthy')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5007)
