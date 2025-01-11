from flask import Flask, jsonify
import random

app = Flask(__name__)

names = ["Alice", "Bob", "Charlie", "Daisy", "Eve"]

@app.route("/name", methods=["GET"])
def get_name():
  return jsonify(name=random.choice(names))

@app.route("/health", methods=["GET"])
def health():
  return jsonify(status="healthy")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001)
