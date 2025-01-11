from flask import Flask, jsonify
import random

app = Flask(__name__)

greetings = ["Hello", "Hi", "Greetings", "Salutations", "Hey"]

@app.route("/greeting", methods=["GET"])
def get_greeting():
  return jsonify(greeting=random.choice(greetings))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5002)
