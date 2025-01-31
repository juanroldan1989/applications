from flask import Flask, jsonify
import random

app = Flask(__name__)

greetings = ["Hello", "Hi", "Greetings", "Salutations", "Hey"]

@app.route("/greeting", methods=["GET"])
def get_greeting():
  return jsonify(greeting=random.choice(greetings))

@app.route('/health', methods=['GET'])
def health():
  return jsonify(status='healthy')

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5002)
